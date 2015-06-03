# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from django.views.generic import TemplateView


urlpatterns = patterns(
    '',
    url(r'^1/$', TemplateView.as_view(template_name='markup/1.html'), name="first"),
    url(r'^2/$', TemplateView.as_view(template_name='markup/2.html'), name="second"),
    url(r'^3/$', TemplateView.as_view(template_name='markup/3.html'), name="third"),
)
