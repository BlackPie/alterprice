# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from product.api import views

urlpatterns = patterns(
    '',
    url(r'^list/$', views.ProductList.as_view(), name='list'),
    url(r'^list/categories/$', views.ProductListCategories.as_view(), name='list-categories'),
    url(r'^list/count/$', views.ProductCount.as_view(), name='list-count'),
    url(r'^detail/(?P<pk>\d+)/offers/$', views.ProductOffers.as_view(), name='offers'),
)
