from django.core.urlresolvers import reverse
from django.views.generic import TemplateView, FormView
from django.utils.translation import ugettext_lazy as _
from django.views.generic.detail import DetailView
from django.utils.decorators import method_decorator
# Project imports
from shop.models import Shop
from client import decorators
from client import forms
from apuser.models import Payment, Bill


class ClientIndexPageView(TemplateView):
    template_name = "apps/client/index.html"

    def get_context_data(self, **kwargs):
        context = super(ClientIndexPageView, self).get_context_data(**kwargs)
        context['current_app'] = 'client-index'
        return context

    @method_decorator(decorators.profile_reverse)
    def dispatch(self, request, *args, **kwargs):
        return super(ClientIndexPageView, self).dispatch(request, *args, **kwargs)


class ClientSignInPageView(TemplateView):
    template_name = "apps/client/login.html"

    def get_context_data(self, **kwargs):
        context = super(ClientSignInPageView, self).get_context_data(**kwargs)
        context['current_app'] = 'client-login'
        context['welcome'] = True
        return context

    @method_decorator(decorators.profile_reverse)
    def dispatch(self, request, *args, **kwargs):
        return super(ClientSignInPageView, self).dispatch(request, *args, **kwargs)


class ClientSignUpPageView(TemplateView):
    template_name = "apps/client/registration.html"

    def get_context_data(self, **kwargs):
        context = super(ClientSignUpPageView, self).get_context_data(**kwargs)
        context['current_app'] = 'client-registration'
        return context

    @method_decorator(decorators.profile_reverse)
    def dispatch(self, request, *args, **kwargs):
        return super(ClientSignUpPageView, self).dispatch(request, *args, **kwargs)


class ClientPasswordResetPageView(TemplateView):
    template_name = "apps/client/password_reset.html"

    def get_context_data(self, **kwargs):
        context = super(ClientPasswordResetPageView, self).get_context_data(**kwargs)
        return context

    @method_decorator(decorators.profile_reverse)
    def dispatch(self, request, *args, **kwargs):
        return super(ClientPasswordResetPageView, self).dispatch(request, *args, **kwargs)


class ClientProfilePageView(TemplateView):
    template_name = "apps/client/profile.html"

    def get_context_data(self, **kwargs):
        context = super(ClientProfilePageView, self).get_context_data(**kwargs)
        context['current_app'] = 'client-profile'
        # context['user'] = self.request.user
        # context['client'] = context['user'].clientprofile_set.first()
        return context

    @method_decorator(decorators.login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(ClientProfilePageView, self).dispatch(request, *args, **kwargs)


class ClientShopAddPageView(TemplateView):
    template_name = "apps/client/shop/add.html"

    def get_context_data(self, **kwargs):
        context = super(ClientShopAddPageView, self).get_context_data(**kwargs)
        context['current_app'] = 'client-shop-add'
        return context

    @method_decorator(decorators.login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(ClientShopAddPageView, self).dispatch(request, *args, **kwargs)


class ClientShopDetailPageView(DetailView):
    model = Shop
    template_name = "apps/client/shop/detail.html"

    def get_context_data(self, **kwargs):
        context = super(ClientShopDetailPageView, self).get_context_data(**kwargs)
        context['current_app'] = 'client-shop-detail'
        return context

    @method_decorator(decorators.login_required)
    def dispatch(self, request, *args, **kwargs):
        # TODO: check that request.user is owner of shop ( self.object )
        return super(ClientShopDetailPageView, self).dispatch(request, *args, **kwargs)


class ClientWalletBalancePageView(TemplateView):
    template_name = "apps/client/wallet/balance.html"

    def get_context_data(self, **kwargs):
        context = super(ClientWalletBalancePageView, self).get_context_data(**kwargs)
        context['refill_history'] = Payment.objects.filter(user=self.request.user.pk)
        context['bills'] = Bill.objects.filter(user=self.request.user.pk)
        context['current_app'] = 'client-shop-add'
        return context

    @method_decorator(decorators.login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(ClientWalletBalancePageView, self).dispatch(request, *args, **kwargs)


class ClientWalletRefillPageView(TemplateView):
    template_name = "apps/client/wallet/refill.html"

    def get_context_data(self, **kwargs):
        context = super(ClientWalletRefillPageView, self).get_context_data(**kwargs)
        context['current_app'] = 'client-wallet-refill'
        return context

    @method_decorator(decorators.login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(ClientWalletRefillPageView, self).dispatch(request, *args, **kwargs)


class ChnageShop(FormView):
    form_class = forms.ChangeShopForm
    template_name = 'change_shop_form.html'

    def get_success_url(self):
        return reverse('client:shop_detail',
                       kwargs={'pk': self.request.session.get('shop_id')})

    def get_initials(self):
        return {'shop': Shop.objects.filter(user=self.request.user)}

    def form_valid(self, form):
        shop = form.cleaned_data.get('shop')
        self.request.session['shop_id'] = shop.id
        # TODO: mb change to revers to HTTP_REFERRER
        return super(ChnageShop, self).form_valid(form)

    @method_decorator(decorators.login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(ChnageShop, self).dispatch(request, *args, **kwargs)


class ClientPricelistDetailPageView(TemplateView):
    template_name = "apps/client/pricelist/detail.html"

    def get_context_data(self, **kwargs):
        context = super(ClientPricelistDetailPageView, self).get_context_data(**kwargs)
        context['current_app'] = 'client-pricelist-detail'
        return context
