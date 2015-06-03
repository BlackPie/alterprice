# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from django.views.generic import TemplateView


urlpatterns = patterns(
    '',
    url(r'^index/$', TemplateView.as_view(template_name='markup/index.html'), name="first"),
    url(r'^categories/$', TemplateView.as_view(template_name='markup/categories_list.html'), name="second"),
    url(r'^items/$', TemplateView.as_view(template_name='markup/items.html'), name="third"),
)
