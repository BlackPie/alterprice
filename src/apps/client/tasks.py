from datetime import datetime, timedelta
from urllib.error import URLError, HTTPError
from urllib.request import urlopen
from celery import shared_task
from celery.task import task, periodic_task
import xmltodict
from client.utils import get_yml_data
from django.core.files.temp import NamedTemporaryFile
from django.core.files.base import File
from django.db.models import Count
from marketapi.api import MarketAPI, MarketHTTPError
from product.models import Product, Offer, ProductPhoto, Opinion
from shop.models.offer import Pricelist, OfferCategories
from celery.utils.log import get_task_logger
from catalog.models.category import Category
from catalog.models.statistics import CategoryStatistics


logger = get_task_logger(__name__)


def load_pictures(pictures, product):
    all_pictures_loaded = True

    if type(pictures) == list:
        for p in pictures:
            try:
                ProductPhoto.objects.make_from_url(p, product)
            except (HTTPError, URLError) as e:
                logger.warn("Cant fetch image: %s" % str(e))
                all_pictures_loaded = False
                continue
    else:
        try:
            ProductPhoto.objects.make_from_url(pictures, product)
        except (HTTPError, URLError) as e:
            all_pictures_loaded = False
            logger.warn("Cant fetch image: %s" % str(e))

    return all_pictures_loaded


def process_pricelist(pricelist_id):
    pricelist = Pricelist.objects.get(id=pricelist_id)
    logger.error('Pricelist "%d" started processing' % pricelist_id)

    try:
        with urlopen(pricelist.yml_url) as f:
            content = f.read()
    except URLError:
        pricelist.status = Pricelist.CANT_PROCESS
        pricelist.save()
        return

    data = xmltodict.parse(content)
    categories, currency, offers = get_yml_data(data)

    try:
        delivery_cost = int(data.get('local_delivery_cost', -1))
    except TypeError:
        delivery_cost = -1

    for offer in offers:
        name = offer.get('name')
        vendor = offer.get('vendor')

        if not name:
            name = offer.get('model')

        logger.error('Offer for "%s" started processing' % name)

        if not name:
            logger.warn("No name present", extra={
                'offer': offer
            })
            continue

        if not vendor or (vendor and vendor.lower() in name.lower()):
            query = '%s' % (name,)
        else:
            query = '%s %s' % (vendor, name,)

        try:
            results = MarketAPI.search_offer(
                query=query.strip(),
                geo_id=225
            )
        except MarketHTTPError:
            logger.warn("Cant fetch results of MarketAPI.search_offer()")
            continue

        try:
            model = results['searchResult']['results'][0]['model']
        except (KeyError, IndexError):
            try:
                model = results['searchResult']['results'][0]['offer']
                model.update({
                    "id": results['searchResult']['results'][0]['offer']['modelId']
                })
            except (KeyError, IndexError):
                continue

        description = model['description']

        try:
            product = Product.objects.get(ym_id=model['id'])
        except Product.DoesNotExist:
            # TODO: hotfix, empty vendor should be handled properly
            if not vendor:
                logger.warn("Vendor is empty", extra={
                    'model': model
                })
                continue

            try:
                product = Product.objects.make(
                    ym_id=model['id'],
                    brand_name=vendor,
                    name=name,
                    category_yml_id=model['categoryId'],
                    description=description
                )
            except MarketHTTPError as e:
                logger.warn("Cant make Product instance: %s" % str(e))
                continue

            pictures = offer.get('picture')

            if pictures:
                if not load_pictures(pictures, product):
                    product.loaded = False
                    product.save()

            try:
                opinions = MarketAPI.get_opinions(model['id'])["modelOpinions"]['opinion']
            except MarketHTTPError as e:
                logger.warn("Cant fetch opinions: %s" % str(e))
                opinions = None

            if opinions:
                opinions_db = []
                for opinion in opinions:
                    opinions_db.append(Opinion(
                        product=product,
                        comment=opinion.get('text'),
                        author=opinion.get('author'),
                        contra=opinion.get('contra'),
                        pro=opinion.get('pro'),
                        grade=opinion.get('grade'),
                        agree=opinion.get('agree'),
                        reject=opinion.get('reject'),
                        ym_id=opinion.get('id'),
                        date=datetime.fromtimestamp(opinion.get('date')/1000),
                    ))
                Opinion.objects.bulk_create(opinions_db)

        try:
            offer_delivery_cost = int(data.get('local_delivery_cost', -1))
        except TypeError:
            offer_delivery_cost = -1

        offer_category = OfferCategories.objects.get_or_create(pricelist=pricelist,
                                                               category=product.category)

        same_offers = Offer.objects.filter(
            shop=pricelist.shop,
            product=product,
        ).order_by('price')

        if same_offers:
            if same_offers[0].price >= float(offer.get('price')):
                continue
            else:
                same_offers.delete()

        offer = Offer.objects.create(
            pricelist=pricelist,
            shop=pricelist.shop,
            url=offer.get('url'),
            price=float(offer.get('price')),
            product=product,
            delivery_cost=offer_delivery_cost if offer_delivery_cost else delivery_cost,
            pickup=bool(offer.get('pickup')),
            offercategory=offer_category
        )
        logger.error('processing success for "%s"' % name)

    pricelist.status = Pricelist.PROCESSED
    pricelist.save()


@shared_task(max_retries=3)
def process_pricelist_task(pricelist_id):
    process_pricelist(pricelist_id)


@periodic_task(run_every=timedelta(days=1))
def refresh_pricelists():
    pricelist_list = Pricelist.objects.all()
    for pricelist in pricelist_list:
        process_pricelist(pricelist.id)


@periodic_task(run_every=timedelta(days=1))
def update_products():
    for product in Product.objects.all():
        try:
            opinions = MarketAPI.get_opinions(product.ym_id)["modelOpinions"]['opinion']
        except MarketHTTPError:
            opinions = []
            logger.error('error when parse opinions for '
                         'product with id "%d"' % product.ym_id)
        opinions_db = []
        for opinion in opinions:
            if Opinion.objects.get(ym_id=opinion['id']):
                continue
            # logger.error(opinion)
            opinions_db.append(Opinion(
                product=product,
                comment=opinion.get('text'),
                author=opinion.get('author'),
                contra=opinion.get('contra'),
                pro=opinion.get('pro'),
                grade=opinion.get('grade'),
                agree=opinion.get('agree'),
                reject=opinion.get('reject'),
                ym_id=opinion.get('id'),
                date=datetime.fromtimestamp(opinion.get('date')/1000),
            ))
        Opinion.objects.bulk_create(opinions_db)
        try:
            details = MarketAPI.get_model_detail(product.ym_id)['modelDetails']
            product.details = details
            product.save()
        except MarketHTTPError:
            logger.error('error when parse details for '
                         'product with id "%d"' % product.ym_id)

@periodic_task(run_every=timedelta(days=1))
def collect_statistics():
    category_list = Category.objects.all()

    for category in category_list:
        click_count = category.product_set.all().aggregate(click_count=Count('offer__click'))['click_count']
        shop_count = category.product_set.all().aggregate(shop_count=Count('offer__shop', distinct=True))['shop_count']
        product_count = category.product_set.count()

        CategoryStatistics.objects.create(
            created=datetime.now().date(),
            click_count=click_count,
            shop_count=shop_count,
            product_count=product_count,
            category=category
        )
