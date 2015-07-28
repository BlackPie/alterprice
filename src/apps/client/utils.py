from django.core.validators import EMPTY_VALUES


def get_yml_data(data):
    if data in EMPTY_VALUES:
        raise Exception('Empty yml')

    catalog = data.get('yml_catalog', None)
    if catalog in EMPTY_VALUES:
        raise Exception('no yml_catalog in file')
    shop = catalog.get('shop', None)
    if shop in EMPTY_VALUES:
        raise Exception('no shop in file')
    offers = shop.get('offers', None)
    offers = offers.get('offer', None)

    if offers in EMPTY_VALUES:
        raise Exception('no offers')
    if not len(offers) > 0:
        raise Exception('no offers')

    categories = shop.get('categories', None)
    categories = categories.get('category', None)
    currency = shop.get('currencies').get('currency')
    return categories, currency, offers