from django.db import models
from datetime import datetime
from django.utils.translation import ugettext_lazy as _


class EnableException(Exception):
    u'''Исключение объекьта на активацию.'''


class DisableException(Exception):
    u'''Исключение объекьта на деактивацию.'''


class StatusModel(models.Model):

    DISABLED = 0
    ENABLED = 1

    STATUS_CHOICES = (
        (DISABLED, _(u'Не активeн')),
        (ENABLED, _(u'Активен')),
    )

    status = models.PositiveSmallIntegerField(verbose_name=_(u'Статус'),
                                              default=ENABLED,
                                              choices=STATUS_CHOICES)

    created = models.DateTimeField(auto_now_add=True,
                                   editable=False,
                                   verbose_name=_(u'Дата создания'))

    def active(self):
        return True if self.status == self.ENABLED else False

    def activate(self):
        if self.active():
            raise EnableException(_(u'Объект уже активен.'))
        else:
            self.status = self.ENABLED
            self.save()

    def deactivate(self):
        if self.active():
            self.status = self.DISABLED
            self.save()
        else:
            raise DisableException(_(u'Объект уже не активен'))

    class Meta:
        abstract = True


class ApprovedModel(models.Model):
    APPROVED = 1
    NOT_APPROVED = 0

    APPROVED_CHOICES = (
        (APPROVED, _(u'Подтвержден')),
        (NOT_APPROVED, _(u'Не подтвержден')),
    )

    approved = models.PositiveSmallIntegerField(verbose_name=_(u'Статус подтвержденности'),
                                                default=NOT_APPROVED,
                                                choices=APPROVED_CHOICES)
    date_approved = models.DateTimeField(null=True,
                                         blank=True,
                                         default=None,
                                         verbose_name=_(u'Дата подтверждения'))
    moderator = models.ForeignKey('apuser.AlterPriceUser',
                                  verbose_name=_('Пользователь'))

    class Meta:
        abstract = True

    @property
    def is_approved(self):
        return True if self.approved == self.APPROVED else False

    def approve(self, moderator=None):
        if not self.is_approved:
            self.approved = self.APPROVED
            self.date_approved = datetime.utcnow()
            # self.moderator = moderator
            self.save()
            return True
        return False


class SendStatusModel(models.Model):
    AWAITING = 0
    SENT = 1
    DECLINED = 2
    # TODO: mb add some status for case of error during sending
    SENDING_STATUS_CHOICES = (
        (AWAITING, _(u'В ожидании')),
        (SENT, _(u'Отправлено')),
        (DECLINED, _(u'Отменено'))
    )

    sending_status = models.PositiveSmallIntegerField(choices=SENDING_STATUS_CHOICES,
                                                      db_index=True,
                                                      default=AWAITING,
                                                      verbose_name=_(u'Статус отправки'))

    sending_date = models.DateTimeField(null=True,
                                        blank=True,
                                        default=None,
                                        verbose_name=_(u'Дата отправки'))

    class Meta:
        abstract = True

    def set_sent(self):
        self.sending_status = self.SENT
        self.sending_date = datetime.utcnow()
        self.save()

    def decline(self):
        self.sending_status = self.DECLINED
        self.save()


class NameModel(models.Model):
    name = models.CharField(max_length=255,
                            verbose_name=_('Название'))

    def __str__(self):
        return '%d: %s' % (self.id, self.name)

    def __unicode__(self):
        return '%d: %s' % (self.id, self.name)

    class Meta:
        abstract = True