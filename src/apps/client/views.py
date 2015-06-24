from django.views.generic import TemplateView
from django.views.generic.detail import DetailView


class ClientIndexPageView(TemplateView):
    template_name = "apps/client/index.html"

    def get_context_data(self, **kwargs):
        context = super(ClientIndexPageView, self).get_context_data(**kwargs)
        return context


class ClientSignInPageView(TemplateView):
    template_name = "apps/client/login.html"

    def get_context_data(self, **kwargs):
        context = super(ClientSignInPageView, self).get_context_data(**kwargs)
        return context


class ClientSignUpPageView(TemplateView):
    template_name = "apps/client/registration.html"

    def get_context_data(self, **kwargs):
        context = super(ClientSignUpPageView, self).get_context_data(**kwargs)
        return context


class ClientPasswordResetPageView(TemplateView):
    template_name = "apps/client/password_reset.html"

    def get_context_data(self, **kwargs):
        context = super(ClientPasswordResetPageView, self).get_context_data(**kwargs)
        return context