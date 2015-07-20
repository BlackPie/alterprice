from shop.models.shop import Shop


def get_shop(request):
        return Shop.objects.filter(user=request.user).first()
    # return request._cached_shop


class ShopMiddleware(object):
    def process_request(self, request):
        if 'shop_id' not in request.session.keys():
            if request.user.is_authenticated():
                shop = Shop.objects.filter(user_id=request.user.id)
                if shop.exists():
                    request.session['shop_id'] = shop.first().id
