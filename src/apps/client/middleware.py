from shop.models import Shop


def get_shop(request):
        return Shop.objects.filter(user=request.user).first()
    # return request._cached_shop


class ShopMiddleware(object):
    def process_request(self, request):
        if 'shop_id' not in request.session.keys():
            shop = Shop.objects.filter(user=request.user)
            if shop.exists():
                request.session['shop_id'] = shop.first().id
