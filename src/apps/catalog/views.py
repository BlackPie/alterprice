import random
from django.views.generic import TemplateView
from product.models import Product
import json


class CatalogAllCategoriesPageView(TemplateView):
    model = Product

    template_name = "apps/catalog/main.html"

    def get_context_data(self, **kwargs):
        context = super(CatalogAllCategoriesPageView, self).get_context_data(**kwargs)
        # context['current_app'] = 'product-detail'
        return context
