# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from shop.api import views

urlpatterns = patterns(
    '',
    url(r'^create/$', views.ShopCreate.as_view(), name='create'),
    url(r'^list/client/$', views.ShopClientList.as_view(), name='client-list'),
)
