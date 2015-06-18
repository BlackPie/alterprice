# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from catalog import views


urlpatterns = patterns(
    '',
    url(r'^$', views.CatalogAllCategoriesPageView.as_view(), name='catalog'),
    url(r'^(?P<pk>\d+)/$', views.CatalogCategoriesListPageView.as_view(), name='detail'),
)

