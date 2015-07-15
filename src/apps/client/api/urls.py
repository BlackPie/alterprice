# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from client.api import views

urlpatterns = patterns(
    '',
    url(r'^signin/$', views.SignInAPIView.as_view(), name='signin'),
    url(r'^signup/$', views.SignUpAPIView.as_view(), name='signup'),
    url(r'^profile/$', views.Profile.as_view(), name='profile'),
    url(r'^profile/password/$', views.ProfilePassword.as_view(), name='profile-password'),
    url(r'^recovery/$', views.Recovery.as_view(), name='recovery'),
    url(r'^recovery/password/$', views.RecoveryPassword.as_view(), name='recovery-password'),
    url(r'^email/update/$', views.UpdateEmail.as_view(), name='email-update'),
    url(r'^invoice/add/$', views.InvoiceRequestView.as_view(), name='invoice-add'),
    url(r'^invoice/list/$', views.InvoiceRequestView.as_view(), name='invoice-add'),
)
