from django.db.models import Q
from django.utils import timezone
from datetime import datetime, timedelta
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from apuser import models


class RegDateFilter(admin.SimpleListFilter):
    title = _('Дата регистрации')
    parameter_name = 'regdate'

    def lookups(self, request, model_admin):
        return (
            ('today', _('Сегодня')),
            ('yesterday', _('Вчера')),
            ('week', _('Неделя')),
            ('two_weeks', _('2 недели')),
            ('three_weeks', _('3 недели')),
            ('month', _('Месяц')),
            ('two_months', _('2 месяца')),
            ('three_months', _('3 месяца')),
            ('six_months', _('6 месяцев')),
            ('year', _('Год'))
        )

    def queryset(self, request, queryset):
        now = timezone.now()
        now = now.replace(hour=0, minute=0, second=0, microsecond=0)
        if self.value() == 'today':
            date_gt = now
            date_lt = date_gt + timedelta(days=1)
            return queryset.filter(created__lt=date_lt, created__gt=date_gt)
        if self.value() == 'yesterday':
            date_lt = now
            date_gt = date_lt - timedelta(days=1)
            return queryset.filter(created__lt=date_lt, created__gt=date_gt)
        if self.value() == 'week':
            date_lt = now + timedelta(days=1)
            date_gt = now - timedelta(days=6)
            return queryset.filter(created__lt=date_lt, created__gt=date_gt)
        if self.value() == 'two_weeks':
            date_lt = now + timedelta(days=1)
            date_gt = now - timedelta(days=13)
            return queryset.filter(created__lt=date_lt, created__gt=date_gt)
        if self.value() == 'three_weeks':
            date_lt = now + timedelta(days=1)
            date_gt = now - timedelta(days=20)
            return queryset.filter(created__lt=date_lt, created__gt=date_gt)
        if self.value() == 'month':
            date_lt = now + timedelta(days=1)
            date_gt = now - timedelta(weeks=4)
            return queryset.filter(created__lt=date_lt, created__gt=date_gt)
        if self.value() == 'two_months':
            date_lt = now + timedelta(days=1)
            date_gt = now - timedelta(weeks=8)
            return queryset.filter(created__lt=date_lt, created__gt=date_gt)
        if self.value() == 'three_months':
            date_lt = now + timedelta(days=1)
            date_gt = now - timedelta(weeks=13)
            return queryset.filter(created__lt=date_lt, created__gt=date_gt)
        if self.value() == 'six_months':
            date_lt = now + timedelta(days=1)
            date_gt = now - timedelta(weeks=26)
            return queryset.filter(created__lt=date_lt, created__gt=date_gt)
        if self.value() == 'year':
            date_lt = now + timedelta(days=1)
            date_gt = now - timedelta(weeks=52)
            return queryset.filter(created__lt=date_lt, created__gt=date_gt)
        return queryset


class UserAdmin(admin.ModelAdmin):
    list_filter = ('user_type', RegDateFilter)

    def queryset(self, request):
        qs = super(UserAdmin, self).queryset(request)
        if not request.is_admin():
            qs = qs.filter(user_type=models.AlterPriceUser.CLIENT)
            qs = qs.filter(Q(clientprofile__operator__isnull=True) | Q(clientprofile__operator=request.user))
        return qs


class ClientAdmin(admin.ModelAdmin):
    def render_change_form(self, request, context, *args, **kwargs):
        operator_qs = models.AlterPriceUser.objects.get_list(operator=True)
        context['adminform'].form.fields['operator'].queryset = operator_qs

        user_qs = models.AlterPriceUser.objects.get_list(client=True)
        context['adminform'].form.fields['user'].queryset = user_qs
        return super(ClientAdmin, self).render_change_form(request, context, args, kwargs)


class OperatorAdmin(admin.ModelAdmin):
    def render_change_form(self, request, context, *args, **kwargs):
        user_qs = models.AlterPriceUser.objects.get_list(operator=True)
        context['adminform'].form.fields['user'].queryset = user_qs
        return super(OperatorAdmin, self).render_change_form(request, context, args, kwargs)


class AdminProfileAdmin(admin.ModelAdmin):
    def render_change_form(self, request, context, *args, **kwargs):
        user_qs = models.AlterPriceUser.objects.get_list(admin=True)
        context['adminform'].form.fields['user'].queryset = user_qs
        return super(AdminProfileAdmin, self).render_change_form(request, context, args, kwargs)        

admin.site.register(models.AlterPriceUser, UserAdmin)
admin.site.register(models.ClientProfile, ClientAdmin)
admin.site.register(models.OperatorProfile, OperatorAdmin)
admin.site.register(models.AdminProfile, AdminProfileAdmin)
