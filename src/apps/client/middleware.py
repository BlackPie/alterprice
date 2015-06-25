from django.utils.functional import SimpleLazyObject
from shop.models import Shop


def get_shop(request):
    if not hasattr(request, '_cached_shop'):
        request._cached_shop = Shop.objects.filter(user=request.user).first()
    return request._cached_shop


class ShopMiddleware(object):
    def process_request(self, request):

        request.shop = SimpleLazyObject(lambda: get_shop(request))
