# -*- coding: utf-8 -*-
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import patterns, include, url
from django.contrib import admin
from alterprice import views


urlpatterns = patterns(
    '',
    url(r'^$', views.IndexView.as_view(), name='index'),

    # APPs
    url(r'^markup/', include('markup.urls', namespace="markup")),
    url(r'^product/', include('product.urls', namespace="product")),
    url(r'^catalog/', include('catalog.urls', namespace="catalog")),
    url(r'^client/', include('client.urls', namespace="client")),


    # API urls
    url(r'^api/product/', include('product.api.urls', namespace="product-api")),
    url(r'^api/catalog/', include('catalog.api.urls', namespace="catalog-api")),
    url(r'^api/brand/', include('brand.api.urls', namespace="brand-api")),
    url(r'^api/shop/', include('shop.api.urls', namespace="shop-api")),
    url(r'^api/user/', include('apuser.api.urls', namespace="user-api")),
    url(r'^api/client/', include('client.api.urls', namespace="client-api")),

    # Aadmin urls
    url(r'^admin/', include(admin.site.urls)),
)


if settings.DEBUG:
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
