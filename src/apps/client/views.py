from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView, FormView
from django.utils.translation import ugettext_lazy as _
from django.views.generic.detail import DetailView
from django import forms
from django.utils.decorators import method_decorator
# Project imports
from shop.models import Shop


class ClientIndexPageView(TemplateView):
    template_name = "apps/client/index.html"

    def get_context_data(self, **kwargs):
        context = super(ClientIndexPageView, self).get_context_data(**kwargs)
        context['current_app'] = 'client-index'
        return context


# decorator reverse profile
class ClientSignInPageView(TemplateView):
    template_name = "apps/client/login.html"

    def get_context_data(self, **kwargs):
        context = super(ClientSignInPageView, self).get_context_data(**kwargs)
        context['current_app'] = 'client-login'
        return context

    def dispatch(self, request, *args, **kwargs):
        return super(ClientSignInPageView, self).dispatch(request, *args, **kwargs)

# decorator reverse profile
class ClientSignUpPageView(TemplateView):
    template_name = "apps/client/registration.html"

    def get_context_data(self, **kwargs):
        context = super(ClientSignUpPageView, self).get_context_data(**kwargs)
        context['current_app'] = 'client-registration'
        return context


# decorator reverse profile
class ClientPasswordResetPageView(TemplateView):
    template_name = "apps/client/password_reset.html"

    def get_context_data(self, **kwargs):
        context = super(ClientPasswordResetPageView, self).get_context_data(**kwargs)
        return context

# decorator login required
class ClientProfilePageView(TemplateView):
    template_name = "apps/client/profile.html"

    def get_context_data(self, **kwargs):
        context = super(ClientProfilePageView, self).get_context_data(**kwargs)
        context['current_app'] = 'client-profile'
        #context['user'] = self.request.user
        #context['client'] = context['user'].clientprofile_set.first()
        return context


# decorator login required
class ClientShopAddPageView(TemplateView):
    template_name = "apps/client/shop/add.html"

    def get_context_data(self, **kwargs):
        context = super(ClientShopAddPageView, self).get_context_data(**kwargs)
        context['current_app'] = 'client-shop-add'
        return context

# decorator login required
class ClientShopDetailPageView(DetailView):
    model = Shop
    template_name = "apps/client/shop/detail.html"

    def get_context_data(self, **kwargs):
        context = super(ClientShopDetailPageView, self).get_context_data(**kwargs)
        context['current_app'] = 'client-shop-detail'
        return context


# decorator login required
class ClientWalletBalancePageView(TemplateView):
    template_name = "apps/client/wallet/balance.html"

    def get_context_data(self, **kwargs):
        context = super(ClientWalletBalancePageView, self).get_context_data(**kwargs)
        context['current_app'] = 'client-shop-add'
        return context


# decorator login required
class ClientWalletRefillPageView(TemplateView):
    template_name = "apps/client/wallet/refill.html"

    def get_context_data(self, **kwargs):
        context = super(ClientWalletRefillPageView, self).get_context_data(**kwargs)
        context['current_app'] = 'client-shop-add'
        return context


class ChangeShopForm(forms.Form):
    shop = forms.ModelChoiceField(
        empty_label=_('Выберете магазин'),
        queryset=Shop.objects.all())


# decorator login required
class ChnageShop(FormView):
    form_class = ChangeShopForm
    template_name = 'change_shop_form.html'

    def get_success_url(self):
        return reverse('client:change-shop')

    def get_initials(self):
        return {'shop': Shop.objects.filter(user=self.request.user)}

    def form_valid(self, form):
        shop = form.cleaned_data.get('shop')
        self.request.session['shop_id'] = shop.id
        return super(ChnageShop, self).form_valid(form)
        # return HttpResponseRedirect(self.request.META.get('HTTP_REFFERER'))
