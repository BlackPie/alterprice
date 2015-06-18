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

    def get_template_names(self):
        if self.object.depth == 1:
            return "apps/catalog/subcategories_list.html"
        return "apps/catalog/categories_list.html"

    def get_context_data(self, **kwargs):
        context = super(CatalogCategoriesListPageView, self).get_context_data(**kwargs)
        context['children_categories'] = self.object.get_children()
        if self.object.parent:
            context['parent_category'] = self.object.parent.pk

        #context['current_app'] = 'product-detail'
        return context


class CatalogCategoryProductListPageView(DetailView):
    model = Category

    template_name = "apps/catalog/category_products_list.html"

    def get_context_data(self, **kwargs):
        context = super(CatalogCategoryProductListPageView, self).get_context_data(**kwargs)
        if self.object.parent:
            context['parent_category'] = self.object.parent.pk
        return context
