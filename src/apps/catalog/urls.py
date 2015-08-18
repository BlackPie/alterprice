# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from catalog import views


urlpatterns = patterns(
    '',
    url(r'^$', views.CatalogAllCategoriesPageView.as_view(), name='categories_list'),
    url(r'^(?P<pk>\d+)/$', views.CatalogCategoriesListPageView.as_view(), name='category_categories_list'),
    url(r'^(?P<pk>\d+)/products/$', views.CatalogCategoryProductListPageView.as_view(), name='category_products_list'),
    url(r'^search/$', views.CatalogSearchProductsPageView.as_view(), name='search_products_list'),
    url(r'statistics/$', views.CategoryStatisticsView.as_view(), name='statistics'),

    url(r'^click/(?P<pk>\d+)/$', views.ClickOffer.as_view(), name='click-offer'),

    # Middleware URL
    url(r'^city/change/$', views.ChangeCity.as_view(), name='change-city'),
)
