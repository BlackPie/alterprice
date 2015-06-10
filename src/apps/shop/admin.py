from django.contrib import admin
from django.contrib.auth import get_user_model
# Project imports
from shop import models
from utils.admin_filters import RegDateFilter
User = get_user_model()


class ShopYMLInline(admin.StackedInline):
    model = models.ShopYML


class ShopAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'user', 'approved')
    inlines = [ShopYMLInline]
    list_filter = (RegDateFilter,)

    def render_change_form(self, request, context, *args, **kwargs):
        user_qs = User.objects.get_list(client=True)
        context['adminform'].form.fields['user'].queryset = user_qs
        return super(ShopAdmin, self).render_change_form(request, context, args, kwargs)

admin.site.register(models.Shop, ShopAdmin)
