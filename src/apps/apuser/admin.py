from django.db.models import Q
from django.utils import timezone
from datetime import datetime, timedelta
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from apuser import models
from utils.admin_filters import RegDateFilter


class OperatorFilter(admin.SimpleListFilter):
    title = _('По личному оператору')
    parameter_name = 'personal_operator'

    def lookups(self, request, model_admin):
        return (
            ('no_operator', _('Без оператора')),
            ('attached_to_me', _('Прикрепленные ко мне')),
        )

    def queryset(self, request, queryset):
        if self.value() == 'no_operator':
            return queryset.filter(operator__isnull=True)
        if self.value() == 'attached_to_me':
            return queryset.filter(operator=request.user)
        return queryset


class BalanceInline(admin.TabularInline):
    model = models.Balance


class UserAdmin(admin.ModelAdmin):
    list_filter = ('user_type', RegDateFilter)
    fields = ('email', 'user_type', 'password')
    inlines = [BalanceInline, ]

    def queryset(self, request):
        qs = super(UserAdmin, self).queryset(request)
        if not request.is_admin():
            qs = qs.filter(user_type=models.AlterPriceUser.CLIENT)
            qs = qs.filter(Q(clientprofile__operator__isnull=True) | Q(clientprofile__operator=request.user))
        else:
            qs = qs.exclude(is_superuser=True)
        return qs


class UserInline(admin.TabularInline):
    model = models.AlterPriceUser


class PaymentInfoInline(admin.StackedInline):
    model = models.ClientPaymentInfo


class ClientAdmin(admin.ModelAdmin):
    # list_display = ('__str__', 'operator', 'approved')
    list_display = ('__str__', 'approved')
    # readonly_fields = ('user', )
    list_filter = (RegDateFilter, OperatorFilter)
    search_fields = ['user__email', 'phone']
    fields = ('user', 'name', 'last_name', 'phone')
    inlines = [PaymentInfoInline, ]

    def queryset(self, request):
        qs = super(ClientAdmin, self).queryset(request)
        if request.user.is_operator():
            qs = qs.filter(user__user_type=models.AlterPriceUser.CLIENT)
            qs = qs.filter(Q(operator__isnull=True) | Q(operator=request.user))
        return qs

    def render_change_form(self, request, context, *args, **kwargs):
        operator_qs = models.AlterPriceUser.objects.get_list(operator=True)
        # context['adminform'].form.fields['operator'].queryset = operator_qs
        user_qs = models.AlterPriceUser.objects.get_list(client=True)
        context['adminform'].form.fields['user'].queryset = user_qs
        return super(ClientAdmin, self).render_change_form(request, context, args, kwargs)


class OperatorAdmin(admin.ModelAdmin):
    readonly_fields = ('code', )
    list_display = ('__str__', 'name', 'last_name')
    list_filter = (RegDateFilter, )

    def render_change_form(self, request, context, *args, **kwargs):
        user_qs = models.AlterPriceUser.objects.get_list(operator=True)
        context['adminform'].form.fields['user'].queryset = user_qs
        return super(OperatorAdmin, self).render_change_form(request, context, args, kwargs)


class AdminProfileAdmin(admin.ModelAdmin):
    def render_change_form(self, request, context, *args, **kwargs):
        user_qs = models.AlterPriceUser.objects.get_list(admin=True)
        context['adminform'].form.fields['user'].queryset = user_qs
        return super(AdminProfileAdmin, self).render_change_form(request, context, args, kwargs)        


class PaymentAdmin(admin.ModelAdmin):
    list_display = ('user', 'amount', 'payment_type', 'created')


class BillAdmin(admin.ModelAdmin):
    list_display = ('user', 'amount', 'created')


admin.site.register(models.Bill, BillAdmin)
admin.site.register(models.Payment, PaymentAdmin)
admin.site.register(models.AlterPriceUser, UserAdmin)
admin.site.register(models.ClientProfile, ClientAdmin)
admin.site.register(models.OperatorProfile, OperatorAdmin)
admin.site.register(models.AdminProfile, AdminProfileAdmin)
