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


@shared_task(max_retries=1)
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
        try:
            category_id = offer.get('categoryId')
            category_obj = list(filter(lambda x: x['@id'] == category_id, categories))[0]
            category = category_obj['#text']
        except IndexError:
            category = ''
        if vendor in name:
            query = '%s %s' % (category, name,)
        else:
            query = '%s %s %s' % (category, vendor, name,)
        results = MarketAPI.search_model(
            query=query.strip(),
            geo_id=225
        )

        try:
            model = list(filter(lambda x: 'model' in x,
                           results['searchResult']['results']))[0]['model']
            product = Product.objects.get(ym_id=model['id'])
        except (IndexError, TypeError):
            logger.error('processing skipped for "%s"' % name)
            continue
        except Product.DoesNotExist:
            product = Product.objects.make(
                ym_id=model['id'],
                brand_name=vendor,
                name=name,
                category_id=model['categoryId'],
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
