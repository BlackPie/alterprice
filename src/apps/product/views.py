import random
from django.db.models import Max, Min, Avg
from django.views.generic.detail import DetailView
from product.models import Product, Offer
import json



class ProductDetailPageView(DetailView):
    model = Product

    template_name = "apps/product/detail.html"

    def get_context_data(self, **kwargs):
        context = super(ProductDetailPageView, self).get_context_data(**kwargs)
        context['current_app'] = 'product-detail'
        # TODO: store in cache
        prices = Offer.objects.filter(product=context['object']) \
            .aggregate(Max('price'), Min('price'), Avg('price'))
        context['price'] = {
            'min': prices['price__min'],
            'max': prices['price__max'],
            'mid': prices['price__avg'],
        }
        context['best_offer'] = self.object.get_best_offer()
        # context['properties'] = self.object.productproperty_set.all()
        context['context'] = json.dumps({
            'productId': context['object'].pk
        })
        return context
