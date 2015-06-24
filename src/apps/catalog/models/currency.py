from django.db import models
from django.utils.translation import ugettext_lazy as _


class CurrencyManager(models.Manager):
    def make(self, codename):
        qs = self.filter(codename=codename)
        if qs.exists():
            return qs.first()
        else:
            obj = self.model()
            obj.codename = codename
            obj.save()
            return obj


class Currency(models.Model):
    codename = models.CharField(max_length=10,
                                unique=True,
                                db_index=True,
                                verbose_name=_('кодовое название'))

    objects = CurrencyManager()

    class Meta:
        verbose_name = _('Валюта')
        verbose_name_plural = _('Валюты')
