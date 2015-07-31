import random
from django.views.generic.detail import DetailView
from product.models import Product
import json



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
        # context['properties'] = self.object.productproperty_set.all()
        context['context'] = json.dumps({
            'productId': context['object'].pk
        })
        return context
