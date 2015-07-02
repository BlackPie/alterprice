# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from shop.api import views

urlpatterns = patterns(
    '',
    url(r'^create/$', views.ShopCreate.as_view(), name='create'),
    url(r'^(?P<pk>\d+)/update$', views.ShopUpdate.as_view(), name='update'),
    url(r'^(?P<pk>\d+)/yml/add/$', views.AddYML.as_view(), name='add-yml'),
    url(r'^list/client/$', views.ShopClientList.as_view(), name='client-list'),
)
