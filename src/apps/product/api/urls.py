# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from product.api import views

urlpatterns = patterns(
    '',
    url(r'^list/$', views.ProductList.as_view(), name='list'),
    url(r'^detail/(?P<pk>\d+)/$', views.ProductDetail.as_view(), name='detail'),

    url(r'^detail/(?P<pk>\d+)/properties/$', views.ProductProperties.as_view(), name='properties'),
)
