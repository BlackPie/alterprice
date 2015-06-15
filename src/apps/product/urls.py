# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from product import views


urlpatterns = patterns(
    '',
    url(r'^detail/(?P<pk>\d+)/$', views.ProductDetailPageView.as_view(), name='detail'),
)

