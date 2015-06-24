# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from django.views.generic import TemplateView


urlpatterns = patterns(
    '',
    url(r'^index/$', TemplateView.as_view(template_name='markup/index.html'), name="first"),
    url(r'^categories/$', TemplateView.as_view(template_name='markup/categories_list.html'), name="second"),
    url(r'^subcategories/$', TemplateView.as_view(template_name='markup/subcategories_list.html'), name="ssecond"),
    url(r'^items/$', TemplateView.as_view(template_name='markup/items.html'), name="third"),
    url(r'^item/$', TemplateView.as_view(template_name='markup/item.html'), name="ololo"),
    url(r'^item-1/$', TemplateView.as_view(template_name='markup/item-1.html'), name="ololo1"),
    url(r'^item-2/$', TemplateView.as_view(template_name='markup/item-2.html'), name="ololo2"),
    url(r'^search/$', TemplateView.as_view(template_name='markup/search.html'), name="search"),
    url(r'^search-empty/$', TemplateView.as_view(template_name='markup/search-empty.html'), name="search-empty"),
    url(r'^agreement/$', TemplateView.as_view(template_name='markup/agreement.html'), name="agreement"),
    url(r'^client/$', TemplateView.as_view(template_name='markup/profile.html'), name="client"),
    url(r'^client-edit/$', TemplateView.as_view(template_name='markup/profile-edit.html'), name="client-edit"),
    url(r'^shop/$', TemplateView.as_view(template_name='markup/shop.html'), name="shop"),
    url(r'^shop-edit/$', TemplateView.as_view(template_name='markup/shop-edit.html'), name="shop-edit"),
    url(r'^payments/$', TemplateView.as_view(template_name='markup/payments.html'), name="payments"),
    url(r'^client-main/$', TemplateView.as_view(template_name='markup/client-main.html'), name="client-main"),
    url(r'^sign-in/$', TemplateView.as_view(template_name='markup/sign_in.html'), name="client-main"),
    url(r'^add-shop/$', TemplateView.as_view(template_name='markup/add-shop.html'), name="add-shop"),
)
