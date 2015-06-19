from django.utils.translation import ugettext_lazy as _
from utils.abstract_models import NameModel


class City(NameModel):
    class Meta:
        verbose_name = _('Город')
        verbose_name_plural = _('Города')
