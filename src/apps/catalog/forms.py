from django import forms
from django.utils.translation import ugettext_lazy as _
from catalog.models.city import City


class ChangeCityForm(forms.Form):
    city = forms.ModelChoiceField(
        empty_label=_('Выберете город'),
        queryset=City.objects.all())
