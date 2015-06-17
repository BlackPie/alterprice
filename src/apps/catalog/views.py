import random
from django.views.generic import TemplateView
from django.views.generic.detail import DetailView
from catalog.models import Category


class CatalogAllCategoriesPageView(TemplateView):
    template_name = "apps/catalog/main.html"

    def get_context_data(self, **kwargs):
        context = super(CatalogAllCategoriesPageView, self).get_context_data(**kwargs)
        # context['current_app'] = 'product-detail'
        return context


class CatalogCategoriesListPageView(DetailView):
    model = Category

    template_name = "apps/catalog/categories_list.html"

    def get_context_data(self, **kwargs):
        context = super(CatalogCategoriesListPageView, self).get_context_data(**kwargs)
        context['children_categories'] = context['object'].get_children()
        #context['current_app'] = 'product-detail'
        return context
