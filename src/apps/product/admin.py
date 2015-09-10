from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
# Project imports
from product import models


class ProductPropertyInline(admin.StackedInline):
    model = models.ProductProperty


class ProductShopInline(admin.StackedInline):
    model = models.Offer


class ProductPhotoInline(admin.StackedInline):
    model = models.ProductPhoto


class ProductFilter(admin.SimpleListFilter):
    title = _("Нераспределённые модели")
    parameter_name = 'product'

    def lookups(self, request, model_admin):
        return (
            ('unfinished', _('Нераспределённые')),
        )

    def queryset(self, request, queryset):
        if self.value() == 'unfinished':
            return queryset.filter(unfinished=True)
        return queryset


class ProductAdmin(admin.ModelAdmin):
    inlines = (ProductPropertyInline, ProductShopInline, ProductPhotoInline)
    list_display = ('__str__', 'created')
    ordering = ('created', )
    list_filter = (ProductFilter,)


admin.site.register(models.Product, ProductAdmin)
admin.site.register(models.ProductPhoto)
admin.site.register(models.Opinion)
admin.site.register(models.Offer)
