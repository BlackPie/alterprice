from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils.translation import ugettext_lazy as _


class AlterPriceUserManager(models.Manager):
    def get_by_natural_key(self, username):
        return self.get(**{self.model.USERNAME_FIELD: username})

    def get_list(self):
        return self.all()

    def make(self):
        return True

    def make_client(self):
        obj = self.make()
        obj.user_type = self.model.CLIENT
        obj.save()
        return obj

    def make_operator(self):
        obj = self.make()
        obj.user_type = self.model.OPERATOR
        obj.save()
        return obj

    def make_admin(self):
        obj = self.make()
        obj.user_type = self.model.ADMIN
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
    name = models.CharField(max_length=150,
                            null=True,
                            blank=True,
                            verbose_name=_(u'Имя'))
    is_staff = models.BooleanField(_(u'Статус сотрудника'),
                                   default=False,
                                   help_text=_(u'Определяет, может ли '
                                               u'пользователь войти в сайт администратора.'))
    user_type = models.PositiveSmallIntegerField(verbose_name=_(u'Статус'),
                                                 default=CLIENT,
                                                 choices=USER_TYPE_CHOICES)

    USERNAME_FIELD = 'email'

    objects = AlterPriceUserManager()

    def __unicode__(self):
        return u'%s: %s' % (self.id, self.email)

    def __str__(self):
        return u'%s: %s' % (self.id, self.email)

    def get_short_name(self):
        return self.name

    def is_client(self):
        return True if self.user_type is self.CLIENT else False

    def is_operator(self):
        return True if self.user_type is self.OPERATOR else False

    def is_admin(self):
        return True if self.user_type is self.ADMI else False

    class Meta:
        verbose_name = _('Пользователь')
        verbose_name_plural = _('Пользователи')
