from django import forms
from django.utils.translation import ugettext_lazy as _
# PRoject imports
from shop.models.shop import Shop


class ChangeShopForm(forms.Form):
    shop = forms.ModelChoiceField(
        empty_label=_('Выберете магазин'),
        queryset=Shop.objects.all())
