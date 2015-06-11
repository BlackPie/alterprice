# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from product.api import views

urlpatterns = patterns(
    '',
    url(r'^list/$', views.ProductListAPIView.as_view(), name='list'),
)
