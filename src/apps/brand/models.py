from django.db import models
from django.utils.translation import ugettext_lazy as _


class Brand(models.Model):
    name = models.CharField(max_length=255,
                            verbose_name=_('Название'))

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = _('Бренд')
        verbose_name_plural = _('Бренды')
