import random
from django.core.validators import EMPTY_VALUES
from django.db import models
from django.utils.translation import ugettext_lazy as _


class BrandManager(models.Manager):
    def get_or_create(self, name):
        try:
            brand = self.get(name__iexact=name)
        except self.model.DoesNotExist:
            brand = Brand(name=name)
            brand.save()
        return brand


class Brand(models.Model):
    name = models.CharField(max_length=255,
                            db_index=True,
                            verbose_name=_('Название'))
    code = models.CharField(max_length=255,
                            # db_index=True,
                            verbose_name=_('VendorCode'),
                            null=True,
                            blank=True)

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name

    objects = BrandManager()

    class Meta:
        verbose_name = _('Бренд')
        verbose_name_plural = _('Бренды')
