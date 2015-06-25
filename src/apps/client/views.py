from django.views.generic import TemplateView
from django.views.generic.detail import DetailView
from shop import Shop


class ClientIndexPageView(TemplateView):
    template_name = "apps/client/index.html"

    def get_context_data(self, **kwargs):
        context = super(ClientIndexPageView, self).get_context_data(**kwargs)
        context['current_app'] = 'client-index'
        return context


class ClientSignInPageView(TemplateView):
    template_name = "apps/client/login.html"

    def get_context_data(self, **kwargs):
        context = super(ClientSignInPageView, self).get_context_data(**kwargs)
        context['current_app'] = 'client-login'
        return context


class ClientSignUpPageView(TemplateView):
    template_name = "apps/client/registration.html"

    def get_context_data(self, **kwargs):
        context = super(ClientSignUpPageView, self).get_context_data(**kwargs)
        context['current_app'] = 'client-registration'
        return context


class ClientPasswordResetPageView(TemplateView):
    template_name = "apps/client/password_reset.html"

    def get_context_data(self, **kwargs):
        context = super(ClientPasswordResetPageView, self).get_context_data(**kwargs)
        return context


class ClientProfilePageView(TemplateView):
    template_name = "apps/client/profile.html"

    def get_context_data(self, **kwargs):
        context = super(ClientProfilePageView, self).get_context_data(**kwargs)
        context['current_app'] = 'client-profile'
        context['user'] = self.request.user
        #context['client'] = context['user'].clientprofile_set.first()
        return context


class ClientShopAddPageView(TemplateView):
    template_name = "apps/client/shop/add.html"

    def get_context_data(self, **kwargs):
        context = super(ClientShopAddPageView, self).get_context_data(**kwargs)
        context['current_app'] = 'client-shop-add'
        return context


class ClientShopDetailPageView(DetailView):
    model = Shop

    template_name = "apps/client/shop/add.html"

    def get_context_data(self, **kwargs):
        context = super(ClientShopDetailPageView, self).get_context_data(**kwargs)
        context['current_app'] = 'client-shop-add'
        return context