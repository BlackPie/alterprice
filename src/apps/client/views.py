from django.http import Http404, HttpResponse
from django.contrib import auth
from django.core.urlresolvers import reverse
from django.views.generic import TemplateView, FormView, RedirectView
from django.views.generic.detail import DetailView
from django.utils.decorators import method_decorator
import json
from django.core.servers.basehttp import FileWrapper
from apuser.models import BalanceHistory, OperatorProfile
from datetime import datetime
from datetime import timedelta
from django.db.models import Sum

from apuser.models.payment import InvoiceRequest
from apuser.models.profile import EmailDelivery
from catalog.models.token import EmailValidation, PasswordRecovery

from client import decorators
from client import forms
from django.conf import settings
from shop.models.offer import Pricelist
from shop.models.shop import Shop


PRICELIST = "price"
SHOP = "shop"
WEEK = 7


class ClientIndexPageView(TemplateView):
    template_name = "apps/client/index.html"

    def get_context_data(self, **kwargs):
        context = super(ClientIndexPageView, self).get_context_data(**kwargs)
        context['current_app'] = 'client-index'
        return context

    @method_decorator(decorators.profile_reverse)
    def dispatch(self, request, *args, **kwargs):
        return super(ClientIndexPageView, self).dispatch(request, *args, **kwargs)


class ClientAgreementsPageView(TemplateView):
    template_name = "apps/client/agreements.html"

    def get_context_data(self, **kwargs):
        context = super(ClientAgreementsPageView, self).get_context_data(**kwargs)
        return context


class ClientContactsPageView(TemplateView):
    template_name = "apps/client/contacts.html"

    def get_context_data(self, **kwargs):
        context = super(ClientContactsPageView, self).get_context_data(**kwargs)
        return context


class ClientSignInPageView(TemplateView):
    template_name = "apps/client/login.html"

    def get_context_data(self, **kwargs):
        context = super(ClientSignInPageView, self).get_context_data(**kwargs)
        context['current_app'] = 'client-login'
        welc = self.request.GET.get('welcome')
        context['welcome'] = True if welc is '' else None
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


class ActivateView(RedirectView):
    permanent = False
    query_string = True

    def get_redirect_url(self, *args, **kwargs):
        token = kwargs.get('token', None)
        emvs = EmailValidation.objects.get_valid(token=token)
        if not emvs.exists():
            raise Http404
        emv = emvs.first()
        emv.confirm()
        user = emv.user
        if not user.is_active:
            user.is_active = True
            user.save()
        EmailDelivery.objects.make(
            template='client/activate.html',
            email=user.email,
        )

        return '%s?welcome' % reverse('client:login')


class ClientPasswordResetPageView(TemplateView):
    template_name = "apps/client/password_reset.html"

    def get_context_data(self, **kwargs):
        context = super(ClientPasswordResetPageView, self).get_context_data(**kwargs)
        context['current_app'] = 'client-reset-password'
        return context

    @method_decorator(decorators.profile_reverse)
    def dispatch(self, request, *args, **kwargs):
        return super(ClientPasswordResetPageView, self).dispatch(request, *args, **kwargs)


class RecoveryPassword(TemplateView):
    template_name = "apps/client/password_new.html"

    def get_context_data(self, **kwargs):
        context = super(RecoveryPassword, self).get_context_data(**kwargs)
        context['current_app'] = 'client-reset-password'
        return context

    def dispatch(self, request, *args, **kwargs):
        token = kwargs.get('token', None)
        if token:
            pr = PasswordRecovery.objects.get_valid(token=token)
            if pr is None:
                raise Http404
        else:
            raise Http404
        return super(RecoveryPassword, self).dispatch(request, *args, **kwargs)


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
        context['current_app'] = 'client-wallet-balance'
        return context

    @method_decorator(decorators.login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(ClientWalletBalancePageView, self).dispatch(request, *args, **kwargs)


class ClientWalletRefillPageView(TemplateView):
    template_name = "apps/client/wallet/refill.html"

    def get_context_data(self, **kwargs):
        context = super(ClientWalletRefillPageView, self).get_context_data(**kwargs)
        context['current_app'] = 'client-wallet-refill'
        context['is_test_pay'] = settings.ROBOKASSA_TEST
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
        context['context'] = json.dumps({'pricelistId': self.kwargs['pk']})
        context['object'] = Pricelist.objects.get(pk=self.kwargs['pk']) #self.kwargs['pk']
        context['current_app'] = 'client-pricelist-detail'
        return context


class ClientPricelistAddPageView(TemplateView):
    template_name = "apps/client/pricelist/add.html"

    def get_context_data(self, **kwargs):
        context = super(ClientPricelistAddPageView, self).get_context_data(**kwargs)
        context['current_app'] = 'client-pricelist-detail'
        return context


class BaseStatisticsView(TemplateView):
    def _get_period_range(self, starting_point, day_num, duration):
        start = starting_point - timedelta(days=day_num)
        start = self._reset_time(start)
        end = start + timedelta(days=duration)
        return start, end

    def _reset_time(self, date):
        return date.replace(second=0, microsecond=0, minute=0, hour=0)

    def _get_period(self):
        now = datetime.now()
        period = self.request.query_params.get('period')
        if period == 'month':
            period_start, period_end = self._get_period_range(now, 30, 30)
        elif period == 'week':
            period_start, period_end = self._get_period_range(now, 7, 7)
        else:
            period_start, period_end = self._get_period_range(now, 1, 1)
        return period_start, period_end

    def _get_obj(self):
        try:
            return self.model.objects.get(pk=self.kwargs.get('pk'))
        except self.model.DoesNotExist:
            raise Http404

    def _get_statistic_by_date(self, statistics_type):
        obj = self._get_obj()
        now = datetime.now()
        result = []

        for x in range(WEEK):
            start, end = self._get_period_range(now, x, 1)

            if statistics_type == SHOP:
                query = BalanceHistory.objects.filter(created__gte=start,
                                                      created__lt=end,
                                                      reason=BalanceHistory.CLICK,
                                                      click__offer__shop=obj)
            elif statistics_type == PRICELIST:
                query = BalanceHistory.objects.filter(created__gte=start,
                                                      created__lt=end,
                                                      reason=BalanceHistory.CLICK,
                                                      click__offer__pricelist=obj)

            clicks_count = query.count()
            money_sum = query.aggregate(Sum('change_value'))
            result.append({
                'date': start.strftime('%d.%m.%y'),
                'clicks_count': clicks_count,
                'money_sum': money_sum['change_value__sum'],
            })

        result.reverse()
        return result


class ClientStatisticShopView(BaseStatisticsView):
    template_name = "apps/client/statistics/shop.html"
    model = Shop

    def get_context_data(self, **kwargs):
        context = super(ClientStatisticShopView, self).get_context_data(**kwargs)
        context['context'] = json.dumps({'shopId': self.request.session.get("shop_id", None), 'pricelistId': False})
        context['current_app'] = 'client-statistics'
        context['by_date'] = self._get_statistic_by_date(statistics_type=SHOP)
        return context


class ClientStatisticPricelistView(BaseStatisticsView):
    model = Pricelist
    template_name = "apps/client/statistics/pricelist.html"

    def get_context_data(self, **kwargs):
        context = super(ClientStatisticPricelistView, self).get_context_data(**kwargs)
        context['object'] = self._get_obj()
        context['context'] = json.dumps({'shopId': False, 'pricelistId': context['object'].pk})
        context['current_app'] = 'client-statistics'
        context['by_date'] = self._get_statistic_by_date(statistics_type=PRICELIST)
        return context


def download_invoice(request, pk):
    try:
        invoicefile = InvoiceRequest.objects.get(id=pk)
    except InvoiceRequest.DoesNotExist:
        raise Http404

    response = HttpResponse(FileWrapper(invoicefile.invoice_file))
    filename = invoicefile.invoice_file.name.split('/')[-1]
    response['Content-Disposition'] = 'attachment; filename=%s' % filename
    return response