import random
from django.views.generic.detail import DetailView
from product.models import Product
import json
from shop.models import Shop, ShopYML


class ProductDetailPageView(DetailView):
    model = Product

    template_name = "apps/product/detail.html"

    def get_context_data(self, **kwargs):
        context = super(ProductDetailPageView, self).get_context_data(**kwargs)
        context['current_app'] = 'product-detail'
        # Faked
        context['price'] = {
            'min': random.randrange(20, 1000),
            'max': random.randrange(1000, 2000),
            'mid': random.randrange(1000, 2000),
        }
        context['best_offer'] = self.object.get_best_offer()
        context['properties'] = self.object.productproperty_set.prefetch_related('propertyinfo_set')
        context['context'] = json.dumps({
            'productId': context['object'].pk
        })
        s = Shop.objects.first()
        ShopYML.objects.make(
            shop=s,
            yml='https://yandex.st/market-export/1.0-17/partner/help/YML.xml'
        )
        return context
