# -*- coding: utf-8 -*-
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import patterns, include, url
from django.contrib import admin
from alterprice import views


urlpatterns = patterns(
    '',
    url(r'^$', views.IndexView.as_view(), name='index'),

    # Aadmin urls
    url(r'^admin/', include(admin.site.urls)),
)


if settings.DEBUG:
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
