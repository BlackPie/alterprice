# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from client.api import views

urlpatterns = patterns(
    '',
    url(r'^signin/$', views.SignInAPIView.as_view(), name='signin'),
    url(r'^signin/welcome/$', views.SignInAPIView.as_view(), name='signin_welcome'),
    url(r'^signup/$', views.SignUpAPIView.as_view(), name='signup'),
    url(r'^profile/$', views.Profile.as_view(), name='profile'),
    url(r'^profile/password/$', views.ProfilePassword.as_view(), name='profile-password'),
    url(r'^recovery/$', views.Recovery.as_view(), name='recovery'),
    url(r'^recovery/password/$', views.RecoveryPassword.as_view(), name='recovery-password'),
    url(r'^email/update/$', views.UpdateEmail.as_view(), name='email-update'),
    url(r'^invoice/add/$', views.InvoiceCreateView.as_view(), name='invoice-add'),
    url(r'^invoice/list/$', views.InvoiceListView.as_view(), name='invoice-list'),
    url(r'^robokassa/add/$', views.RobokassaCreatePaymentAPIView.as_view(), name='robokassa-add'),
    url(r'^robokassa/result/$', views.RobokassaResultAPIView.as_view(), name='robokassa-result'),
    url(r'^market/offer/$', views.RobokassaResultAPIView.as_view(), name='robokassa-result'),
)
