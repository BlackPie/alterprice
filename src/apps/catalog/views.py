from django.http import Http404
from django.core.urlresolvers import reverse
from django.views.generic import TemplateView, FormView, RedirectView
from django.views.generic.detail import DetailView
# Project imports
from catalog.forms import ChangeCityForm
from brand.models import Brand
from catalog.models.category import Category
from catalog.models.city import City
from product.models import Offer
from apuser.models import Click, Balance, BalanceHistory


class CatalogAllCategoriesPageView(TemplateView):
    template_name = "apps/catalog/main.html"

    def get_context_data(self, **kwargs):
        context = super(CatalogAllCategoriesPageView, self).get_context_data(**kwargs)
        return context


class CatalogCategoriesListPageView(DetailView):
    model = Category

    def get_template_names(self):
        if self.object.depth == 1:
            return "apps/catalog/subcategories_list.html"
        return "apps/catalog/categories_list.html"

    def get_context_data(self, **kwargs):
        context = super(CatalogCategoriesListPageView, self).get_context_data(**kwargs)
        context['children_categories'] = self.object.get_children()
        if self.object.parent:
            context['parent_category'] = self.object.parent.pk
        return context


class CatalogCategoryProductListPageView(DetailView):
    model = Category

    template_name = "apps/catalog/category_products_list.html"

    def get_context_data(self, **kwargs):
        context = super(CatalogCategoryProductListPageView, self).get_context_data(**kwargs)
        context['current_app'] = 'catalog-items-list'
        context['brands'] = Brand.objects.all()
        if self.object.parent:
            context['parent_category'] = self.object.parent.pk
        context['children_categories'] = self.object.get_children()
        return context


class CatalogSearchProductsPageView(TemplateView):
    template_name = "apps/catalog/search_products_list.html"

    def get_context_data(self, **kwargs):
        context = super(CatalogSearchProductsPageView, self).get_context_data(**kwargs)
        context['current_app'] = 'catalog-search'
        context['search'] = self.request.GET.get('search', '')
        return context


class ChangeCity(FormView):
    form_class = ChangeCityForm
    template_name = 'change_city_form.html'

    def get_success_url(self):
        return reverse('catalog:categories_list')

    def get_initials(self):
        return {'': City.objects.filter(user=self.request.user)}

    def form_valid(self, form):
        city = form.cleaned_data.get('city')
        self.request.session['city_id'] = city.id
        return super(ChangeCity, self).form_valid(form)


class ClickOffer(RedirectView):
    permanent = False
    query_string = True

    def get_redirect_url(self, *args, **kwargs):
        offer_id = kwargs.get('pk', None)
        psqs = Offer.objects.filter(id=offer_id)
        if not psqs.exists():
            raise Http404
        ps = psqs.first()

        click = Click.objects.make(
            offer=ps,
            user_ip=self.request.META.get('REMOTE_ADDR'))
        user = ps.shop.user

        try:
            balance = user.user.client_profile
        except:
            balance = Balance.objects.make(client=user.client_profile)
        BalanceHistory.objects.decrease(
            balance=balance,
            click=click,
            value=ps.click_price)
        return ps.url

    # def get(self, request, *args, **kwargs):
    #     url = self.get_redirect_url(*args, **kwargs)
    #     if url:
    #         if self.permanent:
    #             return http.HttpResponsePermanentRedirect(url)
    #         else:
    #             return http.HttpResponseRedirect(url)
    #     else:
    #         return http.HttpResponseGone()
