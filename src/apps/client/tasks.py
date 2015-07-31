from urllib.error import URLError
from urllib.request import urlopen
from celery import shared_task
from celery.task import task
import xmltodict
from client.utils import get_yml_data
from marketapi.api import MarketAPI
from product.models import Product, Offer
from shop.models.offer import Pricelist


from celery.utils.log import get_task_logger

logger = get_task_logger(__name__)


@shared_task(max_retries=3)
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

        logger.error('Offer for "%s" started processing' % name)
        # try:
        #     category_id = offer.get('categoryId')
        #     category_obj = list(filter(lambda x: x['@id'] == category_id, categories))[0]
        #     category = category_obj['#text']
        # except IndexError:
        #     category = ''
        if vendor.lower() in name.lower():
            query = '%s' % (name,)
        else:
            query = '%s %s' % (vendor, name,)
        results = MarketAPI.search_offer(
            query=query.strip(),
            geo_id=225
        )

        try:
            model = results['searchResult']['results'][0]['model']
        except (KeyError, IndexError):
            try:
                search_offer = results['searchResult']['results'][0]['offer']
                model = MarketAPI.get_model(search_offer['modelId'], geo_id=225)['model']
            except (IndexError, TypeError, KeyError) as e:
                logger.error('skipped for "%s", %s' % (name, str(e)))
                continue
        if Offer.objects.filter(pricelist_id=pricelist_id, product__ym_id=model['id']):
            continue
        try:
            product = Product.objects.get(ym_id=model['id'])
        except Product.DoesNotExist:
            product = Product.objects.make(
                ym_id=model['id'],
                brand_name=vendor,
                name=name,
                category_yml_id=model['categoryId'],
                description=offer.get('description')
            )
        try:
            offer_delivery_cost = int(data.get('local_delivery_cost', -1))
        except TypeError:
            offer_delivery_cost = -1
        offer = Offer.objects.create(
            pricelist=pricelist,
            shop=pricelist.shop,
            url=offer.get('url'),
            price=float(offer.get('price')),
            product=product,
            delivery_cost=offer_delivery_cost if offer_delivery_cost else delivery_cost,
            pickup=bool(offer.get('pickup'))
        )
        logger.error('processing success for "%s"' % name)

    pricelist.status = Pricelist.PROCESSED
    pricelist.save()
