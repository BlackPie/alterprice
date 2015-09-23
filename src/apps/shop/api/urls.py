# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from shop.api import views

urlpatterns = patterns(
    '',
    url(r'^create/$', views.ShopCreate.as_view(), name='create'),
    url(r'^(?P<pk>\d+)/update$', views.ShopUpdate.as_view(), name='update'),
    url(r'^(?P<pk>\d+)/yml/add/$', views.AddYML.as_view(), name='add-yml'),
    url(r'^list/client/$', views.ShopClientList.as_view(), name='client-list'),

    url(r'^yml/(?P<pk>\d+)/publish/$', views.YMLPublish.as_view(), name='yml-publish'),
    url(r'^yml/(?P<pk>\d+)/unpublish/$', views.YMLUnPublish.as_view(), name='yml-unpulish'),
    url(r'^yml/(?P<pk>\d+)/update/$', views.YMLUpdate.as_view(), name='yml-update'),
    url(r'^yml/(?P<pk>\d+)/delete/$', views.YMLDelete.as_view(), name='yml-delete'),
    url(r'^yml/(?P<pk>\d+)/category/list/$', views.YMLCategoryList.as_view(), name='yml-category-list'),
    url(r'^yml/(?P<pk>\d+)/product/list/$', views.YMLProductList.as_view(), name='yml-product-list'),
    url(r'^yml/(?P<pk>\d+)/info/$', views.YMLInfo.as_view(), name='yml-info'),
    url(r'^category/(?P<pk>\d+)/update/$', views.YMLCategoryUpdate.as_view(), name='yml-category-update'),
    url(r'^statistic/offers/$', views.StatisticOffers.as_view(), name='statistic-offers'),
    url(r'^statistic/categories/$', views.StatisticCategories.as_view(), name='statistic-categories'),

)
