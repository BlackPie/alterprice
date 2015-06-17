# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from brand.api import views

urlpatterns = patterns(
    '',
    url(r'^list/$', views.BrandList.as_view(), name='list'),
)
