from django.utils.translation import ugettext_lazy as _
from django.db import models
from utils.abstract_models import NameModel
from autoslug import AutoSlugField


class City(NameModel):
    slug = AutoSlugField(populate_from='name',
                         unique=True)
    default_city = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if self.default_city:
            try:
                temp = City.objects.get(default_city=True)
                if self != temp:
                    temp.default_city = False
                    temp.save()
            except City.DoesNotExist:
                pass

        super(City, self).save(*args, **kwargs)

    class Meta:
        verbose_name = _('Город')
        verbose_name_plural = _('Города')
