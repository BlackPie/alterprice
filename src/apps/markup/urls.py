# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from django.views.generic import TemplateView


urlpatterns = patterns(
    '',
    url(r'^index/$', TemplateView.as_view(template_name='markup/index.html'), name="first"),
    url(r'^categories/$', TemplateView.as_view(template_name='markup/categories_list.html'), name="second"),
    url(r'^items/$', TemplateView.as_view(template_name='markup/items.html'), name="third"),
    url(r'^item/$', TemplateView.as_view(template_name='markup/item.html'), name="ololo"),
    url(r'^item-1/$', TemplateView.as_view(template_name='markup/item-1.html'), name="ololo1"),
    url(r'^item-2/$', TemplateView.as_view(template_name='markup/item-2.html'), name="ololo2"),
)
