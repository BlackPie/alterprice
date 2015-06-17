from django.contrib import admin
# Project imports
from product import models


class ProductPropertyInline(admin.StackedInline):
    model = models.ProductProperty


class ProductShopInline(admin.StackedInline):
    model = models.ProductShop


class ProductPhotoInline(admin.StackedInline):
    model = models.ProductPhoto


class ProductAdmin(admin.ModelAdmin):
    inlines = (ProductPropertyInline, ProductShopInline, ProductPhotoInline)
    list_display = ('__str__', 'created')
    ordering = ('created', )


admin.site.register(models.Product, ProductAdmin)
admin.site.register(models.PropertyInfo)
admin.site.register(models.ProductShopDelivery)
