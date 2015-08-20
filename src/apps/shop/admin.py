from django.db.models import Q
from django.contrib import admin
from django.contrib.auth import get_user_model
from django.utils.translation import ugettext_lazy as _

from shop import models
from shop.models.offer import Pricelist, OfferCategories
from shop.models.shop import Shop
from utils.admin_filters import CreatedFilter
from apuser.models import profile
User = get_user_model()


class OperatorFilter(admin.SimpleListFilter):
    title = _('По личному оператору')
    parameter_name = 'personal_operator'

    def lookups(self, request, model_admin):
        operators = User.objects.filter(user_type=User.OPERATOR)
        operator_list = list()
        operator_list.append(('me', 'Мои'))
        if operators.exists():
            for o in operators:
                operator_list.append((o.id, o.email))
        return operator_list

    def queryset(self, request, queryset):
        if self.value():
            if self.value() == 'me':
                operator = request.user
            elif self.value().isdigit():
                operator = self.value()
            else:
                return queryset

            client_list = list(profile.ClientProfile.objects.filter(operator=operator))
            user_id_list = [x.user.id for x in client_list]

            if user_id_list:
                queryset = queryset.filter(user__in=user_id_list)
            else:
                queryset = Shop.objects.none()

        return queryset


class ShopYMLInline(admin.StackedInline):
    model = Pricelist


class ShopAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'user', 'raiting')
    inlines = [ShopYMLInline]
    list_filter = (CreatedFilter, OperatorFilter)
    search_fields = ['name', 'user__email', 'user__client_profile__phone']

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
admin.site.register(OfferCategories)
admin.site.register(Pricelist)
