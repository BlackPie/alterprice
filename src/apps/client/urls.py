# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from client import views


urlpatterns = patterns(
    '',
    url(r'^$', views.ClientIndexPageView.as_view(), name='index'),
    url(r'^login/$', views.ClientSignInPageView.as_view(), name='login'),
    url(r'^registration/$', views.ClientSignUpPageView.as_view(), name='registration'),
    url(r'^password_reset/$', views.ClientPasswordResetPageView.as_view(), name='password_reset'),
    url(r'^profile/$', views.ClientProfilePageView.as_view(), name='profile'),
)

