# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from client import views


urlpatterns = patterns(
    '',
    url(r'^$', views.ClientIndexPageView.as_view(), name='index'),
    url(r'^login/$', views.ClientSignInPageView.as_view(), name='login'),
    url(r'^registration/$', views.ClientSignUpPageView.as_view(), name='registration'),
)

