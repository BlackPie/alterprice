from django.contrib import admin
# Project imports
from product import models


class ProductPropertyInline(admin.StackedInline):
    model = models.ProductProperty


class ProductShopInline(admin.StackedInline):
    model = models.ProductShop


class ProductAdmin(admin.ModelAdmin):
    inlines = (ProductPropertyInline, ProductShopInline)
    list_display = ('__str__', 'created')
    ordering = ('created', )


admin.site.register(models.Product, ProductAdmin)
