import time
import hashlib
from datetime import datetime, timedelta
from django.core.validators import EMPTY_VALUES
from django.conf import settings
from django.db import models
from django.utils.translation import ugettext_lazy as _
# Project imports
from utils.abstract_models import SendStatusModel


def recovery_expiration_date(days=None):
    if not days:
        days = settings.RECOVERY_TOKEN_LIFE_DAYS
    return datetime.utcnow() + timedelta(days=days)


def email_expiration_date(days=None):
    if not days:
        days = settings.EMAIL_TOKEN_LIFE_DAYS
    return datetime.utcnow() + timedelta(days=days)


class EmailValidationManager(models.Manager):

    def make(self, email, user, days=None):
        # FIXME: maybe retry three times if generated token is not unique
        expiration_date = email_expiration_date(days)
        obj = self.model(user=user,
                         email=email,
                         token=self.generate_token(email),
                         expiration_date=expiration_date)
        obj.save()
        return obj

    def generate_token(self, email):
        length = settings.EMAIL_TOKEN_LENGHT
        # email = email.encode('utf8')
        # t = '%s' % time.time()
        # t = t.encode('utf8')
        patt = '%s%s' % (email, time)
        patt = patt.encode('utf8')
        return hashlib.md5(patt).hexdigest()[:length]

    def get_expired(self):
        return self.filter(expiration_date__lte=datetime.utcnow())

    def eliminate_expired(self):
        return self.get_expired().delete()

    def get_list(self, token=None, user=None, email=None,
                 is_acting=False, confirmed=False, awaiting=False):
        filters = {}

        filters['status'] = self.model.CONFIRMED if confirmed else self.model.NOT_CONFIRMED
        if token:
            filters['token'] = token
        if email:
            filters['email'] = email
        if user:
            filters['user'] = user
        if is_acting:
            filters['expiration_date__gt'] = datetime.utcnow()
        if awaiting:
            filters['sending_status'] = self.model.AWAITING
        return self.filter(**filters)

    def get_valid(self, token):
        return self.get_list(token=token, is_acting=True)

    def is_valid(self, token):
        qs = self.get_valid(token)
        return qs.first() if qs.exists() else False

    def set_not_relevant(self, email=None, user=None):
        filters = {}
        if email:
            filters['email'] = email
        if user:
            filters['user'] = user
        if filters:
            qs = self.get_list(**filters)
            qs.update(status=self.model.NOT_RELEVANT)

    def sen_qs_sent(self, qs):
        qs.update(sending_status=self.model.SENT)


class EmailValidation(SendStatusModel):
    NOT_CONFIRMED = 0
    CONFIRMED = 1
    NOT_RELEVANT = 2

    STATUS_CHOICES = (
        (NOT_CONFIRMED, 'Не подтвержден'),
        (CONFIRMED, 'Подтвержден'),
        (NOT_RELEVANT, 'Не релевантный')
    )

    user = models.ForeignKey('apuser.AlterPriceUser',
                             verbose_name=_('Пользователь'))
    email = models.EmailField(db_index=True,
                              verbose_name=_('Проверяемый E-mail'))
    token = models.CharField(max_length=255,
                             unique=True,
                             db_index=True,
                             verbose_name=_('Токен активации'))
    status = models.SmallIntegerField(choices=STATUS_CHOICES,
                                      db_index=True,
                                      default=NOT_CONFIRMED,
                                      verbose_name=_('Статус активации'))
    created = models.DateTimeField(auto_now_add=True,
                                   editable=False,
                                   verbose_name=_('Дата создания'))
    confirmed = models.DateTimeField(null=True,
                                     blank=True,
                                     verbose_name=_('Дата подтверждения активации (UTC)'))
    expiration_date = models.DateTimeField(db_index=True,
                                           default=email_expiration_date,
                                           verbose_name=_('Дата истечения'))
    objects = EmailValidationManager()

    def confirm(self):
        self.status = self.CONFIRMED
        self.confirmed = datetime.utcnow()
        self.save()

    def deactivate(self):
        self.status = self.NOT_RELEVANT
        self.save()

    def extend_expiration(self, days=None):
        self.expiration_date = email_expiration_date(days=days)
        self.save()


    def __str__(self):
        return self.email

    def __unicode__(self):
        return self.email

    class Meta:
        verbose_name = _('Активация электронной почты')
        verbose_name_plural = _('Активации электронной почты')


class PasswordRecoveryManager(models.Manager):
    def generate_token(self, email):
        length = settings.RECOVERY_TOKEN_LENGHT
        pat = '%s%s' % (email, time.time())
        return hashlib.md5(pat.encode('utf8')).hexdigest()[:length]

    def make(self, user, days=None):
        if user:
            expiration_date = recovery_expiration_date(days)
            obj = self.model(
                user=user,
                token=self.generate_token(user.email),
                expiration_date=expiration_date,
            )
            obj.save()
            return obj
        return None

    def get_list(self, user=None, token=None, initial=False, awaiting=False):
        filters = {}
        if user:
            filters['user'] = user
        if token not in EMPTY_VALUES:
            filters['token'] = token
        if initial:
            filters['status'] = self.model.INITIAL
        if awaiting:
            filters['sending_status'] = self.model.AWAITING
        if filters:
            return self.filter(**filters)
        return None

    def get_valid(self, token, user=None):
        qs = self.get_list(user=user, token=token)
        qs = qs.filter(status=self.model.INITIAL)
        return qs.first() if qs.exists() else None

    def get_expired(self, user, token):
        qs = self.get_list(user=user, token=token)
        return qs.filter(exp_date__qt=datetime.utcnow())

    def eliminate_expire(self):
        return self.get_expired()

    def sen_qs_sent(self, qs):
        qs.update(sending_status=self.model.SENT)


class PasswordRecovery(SendStatusModel):
    INITIAL = 0
    RECOVERED = 1
    EXPIRED = 2

    STATUS_CHOICES = (
        (INITIAL, _('Выслан')),
        (RECOVERED, _('Восстановлен')),
        (EXPIRED, 'Истек'),
    )

    token = models.CharField(unique=True,
                             max_length=32,
                             verbose_name=_('Токен подтверждения'))
    user = models.ForeignKey('apuser.AlterPriceUser',
                             verbose_name=_('Пользователь'))
    status = models.PositiveSmallIntegerField(choices=STATUS_CHOICES,
                                              default=INITIAL,
                                              db_index=True,
                                              verbose_name=_('Статус'))
    created = models.DateTimeField(auto_now_add=True,
                                   editable=False,
                                   verbose_name=_('Дата создания'))
    expiration_date = models.DateTimeField(db_index=True,
                                           default=recovery_expiration_date,
                                           verbose_name=_('Дата истечения'))
    recovery_date = models.DateTimeField(null=True,
                                         blank=True,
                                         default=None,
                                         verbose_name=_('Дата восстановления'))

    objects = PasswordRecoveryManager()

    def __str__(self):
        return self.user.email

    def __unicode__(self):
        return self.user.email

    def recover(self):
        self.status = self.RECOVERED
        self.date_approved = datetime.utcnow()
        self.save()

    class Meta:
        verbose_name = _('Токен восстановления пароля')
        verbose_name_plural = _('Токены восстановления паролей')
