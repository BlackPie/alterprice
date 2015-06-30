# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from client.api import views

urlpatterns = patterns(
    '',
    url(r'^signin/$', views.SignInAPIView.as_view(), name='signin'),
    url(r'^signup/$', views.SignUpAPIView.as_view(), name='signup'),
    url(r'^recovery/$', views.Recovery.as_view(), name='recovery'),
)
