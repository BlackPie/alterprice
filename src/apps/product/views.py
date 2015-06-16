# -*- coding: utf-8 -*-
from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from product.models import Product


class ProductDetailPageView(DetailView):
    model = Product

    template_name = "apps/product/detail.html"

    def get_context_data(self, **kwargs):
        context = super(ProductDetailPageView, self).get_context_data(**kwargs)
        context['current_app'] = 'product-detail'
        return context