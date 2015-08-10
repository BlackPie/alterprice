from django.db.models import Q
from django.utils import timezone
from datetime import datetime, timedelta
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from apuser import models
from apuser.models.payment import Payment
from utils.admin_filters import CreatedFilter


class AdminPermissionMixin(object):
    def get_model_perms(self, request):
        if request.user.user_type != models.AlterPriceUser.ADMIN:
            return {}
        return super(AdminPermissionMixin, self).get_model_perms(request)


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


class PaymentFilter(admin.SimpleListFilter):
    title = _("Платежи")
    parameter_name = 'payments'

    def lookups(self, request, model_admin):
        return (
            ('from_my_clients', _('Моих клиентов')),
        )

    def queryset(self, request, queryset):
        if self.value() == 'from_my_clients':
            return queryset.filter(client__operator=request.user)
        return queryset


class BalanceInline(admin.TabularInline):
    model = models.Balance


class UserAdmin(admin.ModelAdmin):
    list_filter = ('user_type', CreatedFilter)
    fields = ('email', 'user_type', 'password')
    search_fields = ["email"]
    # inlines = [BalanceInline, ]

    def get_queryset(self, request):
        qs = super(UserAdmin, self).get_queryset(request)
        if not request.user.is_admin():
            qs = qs.filter(user_type=models.AlterPriceUser.CLIENT)
            qs = qs.filter(Q(client_profile__operator__isnull=True) | Q(client_profile__operator=request.user))
        return qs


class UserInline(admin.TabularInline):
    model = models.AlterPriceUser


class PaymentInfoInline(admin.StackedInline):
    model = models.ClientPaymentInfo


class ClientAdmin(admin.ModelAdmin):
    # list_display = ('__str__', 'operator', 'approved')
    list_display = ('__str__', 'checked', 'is_active')
    # readonly_fields = ('user', )
    list_filter = (CreatedFilter, OperatorFilter)
    search_fields = ['user__email', 'phone', 'company']
    fields = ('user', 'name', 'last_name', 'phone', 'checked', 'is_active',
              'ownership_type', 'company', 'operator', 'city')
    inlines = [PaymentInfoInline, BalanceInline]

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


class OperatorAdmin(AdminPermissionMixin, admin.ModelAdmin):
    readonly_fields = ('code', )
    list_display = ('__str__', 'name', 'last_name')
    list_filter = (CreatedFilter, )
    search_fields = ['user__email', 'phone']

    def render_change_form(self, request, context, *args, **kwargs):
        user_qs = models.AlterPriceUser.objects.get_list(operator=True)
        context['adminform'].form.fields['user'].queryset = user_qs
        return super(OperatorAdmin, self).render_change_form(request, context, args, kwargs)


class AdminProfileAdmin(AdminPermissionMixin, admin.ModelAdmin):
    search_fields = ['user__email', 'phone']

    def render_change_form(self, request, context, *args, **kwargs):
        user_qs = models.AlterPriceUser.objects.get_list(admin=True)
        context['adminform'].form.fields['user'].queryset = user_qs
        return super(AdminProfileAdmin, self).render_change_form(request, context, args, kwargs)


class PaymentAdmin(admin.ModelAdmin):
    exclude = ('payment_type', 'robokassa_success')
    list_display = ('client', 'amount', 'created', 'currency', 'payment_status')
    list_filter = (PaymentFilter,)

    def save_model(self, request, obj, form, change):
        obj.save()
        try:
            balance = obj.client.balance
        except AttributeError:
            balance = models.Balance.objects.make(client=obj.user.client_profile)
        if obj.is_payment():
            models.BalanceHistory.objects.increase(
                payment=obj,
                balance=balance)
        if obj.is_recovery():
            models.BalanceHistory.objects.recover(
                balance=balance,
                payment=obj)


class BalanceHistoryAdmin(admin.ModelAdmin):
    list_display = ('balance', 'change_value', 'reason', 'created')


admin.site.register(models.BalanceHistory, BalanceHistoryAdmin)
admin.site.register(Payment, PaymentAdmin)
admin.site.register(models.AlterPriceUser, UserAdmin)
admin.site.register(models.ClientProfile, ClientAdmin)
admin.site.register(models.OperatorProfile, OperatorAdmin)
admin.site.register(models.AdminProfile, AdminProfileAdmin)
admin.site.register(models.InvoiceRequest)
admin.site.register(models.Balance)
