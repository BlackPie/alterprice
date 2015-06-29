from django.core.validators import EMPTY_VALUES
from django.db import models
from django.db.models.query import QuerySet
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils.translation import ugettext_lazy as _


class AlterPriceUserQueryset(QuerySet):
    def by_email(self, email):
        return self.filter(email=email)


class AlterPriceUserManager(models.Manager):
    def get_by_natural_key(self, username):
        return self.get(**{self.model.USERNAME_FIELD: username})

    def get_list(self, client=False, operator=False, admin=False):
        filters = {}
        if client:
            filters['user_type'] = self.model.CLIENT
        if operator:
            filters['user_type'] = self.model.OPERATOR
        if admin:
            filters['user_type'] = self.model.ADMIN
        if filters not in EMPTY_VALUES:
            qs = self.filter(**filters)
        else:
            qs = self.all()
        return qs

    def make(self, email, password):
        obj = self.model()
        obj.email = email
        obj.set_password(password)
        obj.save()
        return obj

    def make_client(self):
        obj = self.make()
        obj.user_type = self.model.CLIENT
        obj.save()
        return obj

    def make_operator(self):
        obj = self.make()
        obj.user_type = self.model.OPERATOR
        obj.is_staff = True
        obj.save()
        return obj

    def make_admin(self):
        obj = self.make()
        obj.user_type = self.model.ADMIN
        obj.is_staff = True
        obj.save()
        return obj


class AlterPriceUser(AbstractBaseUser, PermissionsMixin):

    CLIENT = 0
    OPERATOR = 1
    ADMIN = 2

    USER_TYPE_CHOICES = (
        (CLIENT, _('Клиент')),
        (OPERATOR, _('Оператор')),
        (ADMIN, _('Администратор')),
    )

    email = models.EmailField(max_length=100,
                              db_index=True,
                              unique=True,
                              verbose_name=_(u'Электронная почта'))
    is_staff = models.BooleanField(_(u'Статус сотрудника'),
                                   default=False,
                                   help_text=_(u'Определяет, может ли '
                                               u'пользователь войти в сайт администратора.'))
    user_type = models.PositiveSmallIntegerField(verbose_name=_(u'Статус'),
                                                 default=CLIENT,
                                                 choices=USER_TYPE_CHOICES)
    created = models.DateTimeField(auto_now_add=True,
                                   editable=False,
                                   verbose_name=_(u'Дата регистрации'))

    USERNAME_FIELD = 'email'

    objects = AlterPriceUserManager.from_queryset(AlterPriceUserQueryset)()

    def __unicode__(self):
        return self.email

    def __str__(self):
        return self.email

    def get_short_name(self):
        return self.email

    def is_client(self):
        return True if self.user_type is self.CLIENT else False

    def is_operator(self):
        return True if self.user_type is self.OPERATOR else False

    def is_admin(self):
        return True if self.user_type is self.ADMI else False

    def get_shops(self):
        return self.owner.all()

    class Meta:
        verbose_name = _('Пользователь')
        verbose_name_plural = _('Пользователи')
