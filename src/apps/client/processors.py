from shop.models.shop import Shop


def shop_processor(request):
    qs = Shop.objects.filter(id=request.session.get('shop_id'))
    current_shop = qs.first() if qs.exists() else None
    return {'current_shop': current_shop}
