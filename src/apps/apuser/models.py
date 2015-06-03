from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils.translation import ugettext_lazy as _


class AlterPriceUserManager(models.Manager):
    def get_list(self):
        return self.all()

    def make(self):
        return True


class AlterPriceUser(AbstractBaseUser, PermissionsMixin):
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

    USERNAME_FIELD = 'email'

    objects = AlterPriceUserManager()

    def __unicode__(self):
        return u'%s: %s' % (self.id, self.email)

    def __str__(self):
        return u'%s: %s' % (self.id, self.email)

    class Meta:
        verbose_name = _('Пользователь')
        verbose_name_plural = _('Пользователи')
