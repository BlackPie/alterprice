from django.conf import settings
from django.core.urlresolvers import reverse_lazy
from django.conf.urls import patterns, include, url
from client import views


urlpatterns = patterns(
    '',
    url(r'^$', views.ClientIndexPageView.as_view(), name='index'),
    # auth urls
    url(r'^login/$', views.ClientSignInPageView.as_view(), name='login'),
    url(r'^signout/$',
        'django.contrib.auth.views.logout',
        {'next_page': reverse_lazy('client:index'), },
        name='signout'),
    url(r'^registration/$', views.ClientSignUpPageView.as_view(), name='registration'),
    url(r'^password_reset/$', views.ClientPasswordResetPageView.as_view(), name='password_reset'),

    url(r'^activate/(?P<token>%s)/$' % settings.EMAIL_TOKEN_PATTERN,
        views.ActivateView.as_view(),
        name='activate-link'),
    url(r'^password/(?P<token>%s)/$' % settings.RECOVERY_TOKEN_PATTERN,
        views.RecoveryPassword.as_view(),
        name="recovery-link"),

    # cabinet urls
    url(r'^profile/$', views.ClientProfilePageView.as_view(), name='profile'),
    url(r'^shop/add/$', views.ClientShopAddPageView.as_view(), name='shop_add'),
    url(r'^shop/(?P<pk>\d+)/$', views.ClientShopDetailPageView.as_view(), name='shop_detail'),
    url(r'^wallet/balance/$', views.ClientWalletBalancePageView.as_view(), name='wallet_balance'),
    url(r'^wallet/refill/$', views.ClientWalletRefillPageView.as_view(), name='wallet_refill'),
    url(r'^statistics/$', views.ClientStatisticsDetailPageView.as_view(), name='statistics_detail'),
    url(r'^pricelist/(?P<pk>\d+)/$', views.ClientPricelistDetailPageView.as_view(), name='pricelist_detail'),
    url(r'^pricelist/add/$', views.ClientPricelistAddPageView.as_view(), name='pricelist_add'),

    # Middleware UL
    url(r'^shop/change/$', views.ChnageShop.as_view(), name='change-shop'),
)
