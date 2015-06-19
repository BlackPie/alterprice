from django.utils.translation import ugettext_lazy as _
from utils.abstract_models import NameModel
from autoslug import AutoSlugField


class City(NameModel):
    slug = AutoSlugField(populate_from='name',
                         unique=True)

    class Meta:
        verbose_name = _('Город')
        verbose_name_plural = _('Города')
