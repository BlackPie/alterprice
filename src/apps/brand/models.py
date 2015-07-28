import random
from django.core.validators import EMPTY_VALUES
from django.db import models
from django.utils.translation import ugettext_lazy as _


class BrandManager(models.Manager):
    def get_or_create(self, name):
        try:
            brand = self.get(name__iexact=name)
        except self.DoesNotExist:
            brand = Brand(name=name)
            brand.save()
        return brand

    def make_from_yml(self, yml_obj):
        obj = None
        code = yml_obj.get('vendorCode')
        if code not in EMPTY_VALUES:
            qs = self.filter(code=code)
            if qs.exists():
                obj = qs.first()
            else:
                name = yml_obj.get('vendor')
                if name:
                    obj = self.model()
                    obj.name = name
                    obj.code = code
                    obj.save()
        return obj


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
