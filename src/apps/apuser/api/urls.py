# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from apuser.api import views

urlpatterns = patterns(
    '',
    url(r'^payment/list/$', views.PaymentList.as_view(), name='payment-list'),
)
