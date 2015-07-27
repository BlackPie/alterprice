from django.db import models
from django.utils.translation import ugettext_lazy as _
# Project imports
from product.models import Offer


class MakeException(Exception):
    ""


class ClickManager(models.Manager):
    def make(self, offer, user_ip):
        if not isinstance(offer, Offer):
            raise MakeException('invalid offer object')
        obj = self.model()
        obj.offer = offer
        obj.user_ip = user_ip
        obj.save()
        return obj


class Click(models.Model):
    created = models.DateTimeField(auto_now_add=True,
                                   editable=False,
                                   verbose_name=_('Дата создания'))
    offer = models.ForeignKey(Offer,
                              verbose_name=_('Предложение'),
                              null=True,
                              blank=True)
    user_ip = models.GenericIPAddressField(max_length=255,
                                           null=True,
                                           blank=True,
                                           default=None,
                                           verbose_name=_('IP пользователя'))

    objects = ClickManager()

    class Meta:
        verbose_name = _('Клик по товару')
        verbose_name_plural = _('Клики по товару')
