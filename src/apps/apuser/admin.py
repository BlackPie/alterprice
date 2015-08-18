import operator
from functools import reduce

from django.db.models import Q
from django.utils import timezone
from datetime import datetime, timedelta
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from django.contrib.admin.utils import lookup_needs_distinct
from apuser import models
from apuser.models.payment import Payment
from utils.admin_filters import CreatedFilter, ProfileCreatedFilter


class AdminPermissionMixin(object):
    def get_model_perms(self, request):
        if request.user.user_type != models.AlterPriceUser.ADMIN:
            return {}
        return super(AdminPermissionMixin, self).get_model_perms(request)


class StrictSearchMixin(object):
    def get_search_results(self, request, queryset, search_term):
        def construct_search(field_name):
            if field_name.startswith('^'):
                return "%s__istartswith" % field_name[1:]
            elif field_name.startswith('@'):
                return "%s__search" % field_name[1:]
            else:
                return "%s__iexact" % field_name

        use_distinct = False
        search_fields = self.get_search_fields(request)
        if search_fields and search_term:
            orm_lookups = [construct_search(str(search_field)) for search_field in search_fields]

            for bit in search_term.split():
                or_queries = [Q(**{orm_lookup: bit})
                              for orm_lookup in orm_lookups]
                queryset = queryset.filter(reduce(operator.or_, or_queries))

            if not use_distinct:
                for search_spec in orm_lookups:
                    if lookup_needs_distinct(self.opts, search_spec):
                        use_distinct = True
                        break

        return queryset, use_distinct


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


class UserAdmin(StrictSearchMixin, admin.ModelAdmin):
    list_filter = ('user_type', CreatedFilter)
    fields = ('email', 'user_type', 'password', 'verified')
    search_fields = ["email"]
    # inlines = [BalanceInline, ]

    def get_queryset(self, request):
        qs = super(UserAdmin, self).get_queryset(request)
        if not request.user.is_admin():
            qs = qs.filter(user_type=models.AlterPriceUser.CLIENT)
            qs = qs.filter(Q(client_profile__operator__isnull=True) | Q(client_profile__operator=request.user))
        return qs

    def save_model(self, request, obj, form, change):
        models.AlterPriceUser.objects.make_user(email=form.cleaned_data['email'],
                                                password=form.cleaned_data['password'],
                                                user_type=form.cleaned_data['user_type'])


class UserInline(admin.TabularInline):
    model = models.AlterPriceUser


class PaymentInfoInline(admin.StackedInline):
    model = models.ClientPaymentInfo


class ClientAdmin(StrictSearchMixin, admin.ModelAdmin):
    # list_display = ('__str__', 'operator', 'approved')
    list_display = ('__str__', 'checked', 'is_active')
    # readonly_fields = ('user', )
    list_filter = (ProfileCreatedFilter, OperatorFilter)
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


class OperatorAdmin(StrictSearchMixin, AdminPermissionMixin, admin.ModelAdmin):
    readonly_fields = ('code', )
    list_display = ('__str__', 'name', 'last_name')
    list_filter = (ProfileCreatedFilter, )
    search_fields = ['user__email', 'phone']

    def render_change_form(self, request, context, *args, **kwargs):
        user_qs = models.AlterPriceUser.objects.get_list(operator=True)
        context['adminform'].form.fields['user'].queryset = user_qs
        return super(OperatorAdmin, self).render_change_form(request, context, args, kwargs)


class AdminProfileAdmin(StrictSearchMixin, AdminPermissionMixin, admin.ModelAdmin):
    search_fields = ['user__email', 'phone']
    list_filter = (ProfileCreatedFilter, )

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
            balance = models.Balance.objects.make(client=obj.client)

        if obj.payment_status == obj.PAID:
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
admin.site.register(models.Click)
