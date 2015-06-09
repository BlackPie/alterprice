from django.contrib import admin
from django.contrib.auth import get_user_model
from shop import models
User = get_user_model()


class ShopAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'user',)

    def render_change_form(self, request, context, *args, **kwargs):
        user_qs = User.objects.get_list(client=True)
        context['adminform'].form.fields['user'].queryset = user_qs
        return super(ShopAdmin, self).render_change_form(request, context, args, kwargs)

admin.site.register(models.Shop, ShopAdmin)
