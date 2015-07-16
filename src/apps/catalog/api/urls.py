# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from catalog.api import views

urlpatterns = patterns(
    '',
    url(r'^category/list/$', views.CategoryList.as_view(), name='category-list'),
    url(r'^cities/list/$', views.CitiesList.as_view(), name='cities-list'),
)
