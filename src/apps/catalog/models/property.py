from django.db import models
from django.utils.translation import ugettext_lazy as _


class PropertyManager(models.Manager):
    def make(self, codename, ru_name=None):
        qs = self.filter(codename=codename)
        if qs.exists():
            return qs.first()
        else:
            obj = self.model()
            obj.codename = codename
            obj.ru_name = ru_name
            obj.save()
            return obj


class Property(models.Model):
    codename = models.CharField(max_length=255,
                                db_index=True,
                                unique=True,
                                verbose_name=_('Кодовое имя'))
    ru_name = models.CharField(max_length=255,
                               blank=True,
                               null=True,
                               default=None,
                               verbose_name=_('Русское название'))

    objects = PropertyManager()

    def __str__(self):
        return self.codename

    def __unicode__(self):
        return self.codename

    class Meta:
        verbose_name = _('Свойство продуктов')
        verbose_name_plural = _('Свойства продуктов')
