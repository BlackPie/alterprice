from datetime import timedelta
from django.utils import timezone
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _


class CreatedFilter(admin.SimpleListFilter):
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
            return queryset.filter(created__lt=date_lt,
                                   created__gt=date_gt)
        if self.value() == 'yesterday':
            date_lt = now
            date_gt = date_lt - timedelta(days=1)
            return queryset.filter(created__lt=date_lt,
                                   created__gt=date_gt)
        if self.value() == 'week':
            date_lt = now + timedelta(days=1)
            date_gt = now - timedelta(days=6)
            return queryset.filter(created__lt=date_lt,
                                   created__gt=date_gt)
        if self.value() == 'two_weeks':
            date_lt = now + timedelta(days=1)
            date_gt = now - timedelta(days=13)
            return queryset.filter(created__lt=date_lt,
                                   created__gt=date_gt)
        if self.value() == 'three_weeks':
            date_lt = now + timedelta(days=1)
            date_gt = now - timedelta(days=20)
            return queryset.filter(created__lt=date_lt,
                                   created__gt=date_gt)
        if self.value() == 'month':
            date_lt = now + timedelta(days=1)
            date_gt = now - timedelta(weeks=4)
            return queryset.filter(created__lt=date_lt,
                                   created__gt=date_gt)
        if self.value() == 'two_months':
            date_lt = now + timedelta(days=1)
            date_gt = now - timedelta(weeks=8)
            return queryset.filter(created__lt=date_lt,
                                   created__gt=date_gt)
        if self.value() == 'three_months':
            date_lt = now + timedelta(days=1)
            date_gt = now - timedelta(weeks=13)
            return queryset.filter(created__lt=date_lt,
                                   created__gt=date_gt)
        if self.value() == 'six_months':
            date_lt = now + timedelta(days=1)
            date_gt = now - timedelta(weeks=26)
            return queryset.filter(created__lt=date_lt,
                                   created__gt=date_gt)
        if self.value() == 'year':
            date_lt = now + timedelta(days=1)
            date_gt = now - timedelta(weeks=52)
            return queryset.filter(created__lt=date_lt,
                                   created__gt=date_gt)
        return queryset


# TODO
class ProfileCreatedFilter(admin.SimpleListFilter):
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
            return queryset.filter(user__created__lt=date_lt,
                                   user__created__gt=date_gt)
        if self.value() == 'yesterday':
            date_lt = now
            date_gt = date_lt - timedelta(days=1)
            return queryset.filter(user__created__lt=date_lt,
                                   user__created__gt=date_gt)
        if self.value() == 'week':
            date_lt = now + timedelta(days=1)
            date_gt = now - timedelta(days=6)
            return queryset.filter(user__created__lt=date_lt,
                                   user__created__gt=date_gt)
        if self.value() == 'two_weeks':
            date_lt = now + timedelta(days=1)
            date_gt = now - timedelta(days=13)
            return queryset.filter(user__created__lt=date_lt,
                                   user__created__gt=date_gt)
        if self.value() == 'three_weeks':
            date_lt = now + timedelta(days=1)
            date_gt = now - timedelta(days=20)
            return queryset.filter(user__created__lt=date_lt,
                                   user__created__gt=date_gt)
        if self.value() == 'month':
            date_lt = now + timedelta(days=1)
            date_gt = now - timedelta(weeks=4)
            return queryset.filter(user__created__lt=date_lt,
                                   user__created__gt=date_gt)
        if self.value() == 'two_months':
            date_lt = now + timedelta(days=1)
            date_gt = now - timedelta(weeks=8)
            return queryset.filter(user__created__lt=date_lt,
                                   user__created__gt=date_gt)
        if self.value() == 'three_months':
            date_lt = now + timedelta(days=1)
            date_gt = now - timedelta(weeks=13)
            return queryset.filter(user__created__lt=date_lt,
                                   user__created__gt=date_gt)
        if self.value() == 'six_months':
            date_lt = now + timedelta(days=1)
            date_gt = now - timedelta(weeks=26)
            return queryset.filter(user__created__lt=date_lt,
                                   user__created__gt=date_gt)
        if self.value() == 'year':
            date_lt = now + timedelta(days=1)
            date_gt = now - timedelta(weeks=52)
            return queryset.filter(user__created__lt=date_lt,
                                   user__created__gt=date_gt)
        return queryset