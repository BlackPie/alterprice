import logging

from django import template
from django.core.urlresolvers import reverse_lazy
register = template.Library()


logger = logging.getLogger(__name__)


@register.filter
def get_breadcrumbs_by_product(object):
    try:
        categories_list = []
        categories_list.append(object)
        if object.category:
            categories_list.append(object.category)
            if object.category.parent:
                categories_list.append(object.category.parent)
                if object.category.parent.parent:
                    categories_list.append(object.category.parent.parent)
                    if object.category.parent.parent.parent:
                        categories_list.append(object.category.parent.parent.parent)
        result = []
        i = 0
        for category in reversed(categories_list):
            if i == 0:
                url = reverse_lazy('catalog:category_categories_list', kwargs={'pk': category.pk},)
            else:
                if i == 1:
                    url = reverse_lazy('catalog:category_categories_list', kwargs={'pk': category.pk},)
                else:
                    url = reverse_lazy('catalog:category_products_list', kwargs={'pk': category.pk},)
            result.append({'object': category, 'url': url})
            i = i + 1
        return result
    except: pass
    return []