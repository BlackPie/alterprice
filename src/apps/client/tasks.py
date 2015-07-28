from urllib.error import URLError
from urllib.request import urlopen
from celery.task import task
import xmltodict
from client.utils import get_yml_data
from marketapi.api import MarketAPI
from product.models import Product, Offer
from shop.models.offer import Pricelist


@task(max_retries=3)
def process_pricelist(pricelist_id):
    pricelist = Pricelist.objects.get(id=pricelist_id)
    try:
        with urlopen(pricelist.yml_url) as f:
            content = f.read()
    except URLError:
        pricelist.status = Pricelist.CANT_PROCESS
        pricelist.save()
        return

    categories, currency, offers = get_yml_data(xmltodict.parse(content))

    for offer in offers:
        name = offer.get('name')
        vendor = offer.get('vendor')
        try:
            category_id = offer.get('categoryId')
            category_obj = list(filter(lambda x: x['@id'] == category_id, categories))[0]
            category = category_obj['#text']
        except IndexError:
            category = ''
        if vendor in name:
            query = '%s %s' % ('', name,)
        else:
            query = '%s %s %s' % ('', vendor, name,)
        results = MarketAPI.search_model(
            query=query,
            geo_id=225
        )

        try:
            model = list(filter(lambda x: 'model' in x,
                           results['searchResult']['results']))[0]
            product = Product.objects.get(ym_id=model['model']['id'])
        except IndexError:
            continue
        except Product.DoesNotExist:
            product = Product.objects.make(
                ym_id=model['ym_id'],
                brand_name=vendor,
                name=name,
                category_id=model['categoryId'],
                description=offer.get('description')
            )
        offer = Offer.objects.create(
            pricelist=pricelist,
            shop=pricelist.shop,
            url=offer.get('url'),
            price=float(offer.get('price')),
            product=product,
        )
    pricelist.status = Pricelist.PROCESSED
    pricelist.save()
