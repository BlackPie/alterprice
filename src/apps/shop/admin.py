from django.db.models import Q
from django.contrib import admin
from django.contrib.auth import get_user_model
from django.utils.translation import ugettext_lazy as _

from shop import models
from shop.models.offer import Pricelist
from shop.models.shop import Shop
from utils.admin_filters import RegDateFilter
User = get_user_model()


class OperatorFilter(admin.SimpleListFilter):
    title = _('По личному оператору')
    parameter_name = 'personal_operator'

    def lookups(self, request, model_admin):
        operators = User.objects.filter(user_type=User.OPERATOR)
        lkps = list()
        lkps.append(('asd', 'asd'))
        if operators.exists():
            for o in operators:
                lkps.append((o.id, o.email))
        return lkps

    def queryset(self, request, queryset):
        return queryset


class ShopYMLInline(admin.StackedInline):
    model = Pricelist


class ShopAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'user', 'raiting')
    inlines = [ShopYMLInline]
    list_filter = (RegDateFilter, OperatorFilter)

    def render_change_form(self, request, context, *args, **kwargs):
        user_qs = User.objects.get_list(client=True)
        context['adminform'].form.fields['user'].queryset = user_qs
        return super(ShopAdmin, self).render_change_form(request, context, args, kwargs)

    def queryset(self, request):
        qs = super(ShopAdmin, self).queryset(request)
        if request.user.is_operator():
            # TODO: test
            qs = qs.filter(
                Q(user__clientprofile__operator=request.user) |
                Q(user__clientprofile__operator__isnull=True)
            )
        return qs


admin.site.register(Shop, ShopAdmin)
