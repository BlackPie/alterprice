from django.db.models import Q
from django.http import Http404
from django.core.urlresolvers import reverse
from django.views.generic import TemplateView, FormView, RedirectView
from django.views.generic.detail import DetailView
from datetime import datetime, date
# Project imports
from catalog.forms import ChangeCityForm
from brand.models import Brand
from catalog.models.category import Category
from catalog.models.city import City
from product.models import Offer
from apuser.models import Click, Balance, BalanceHistory
from catalog.models.statistics import CategoryStatistics
from shop.models.shop import Shop


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
        context['brands'] = Brand.objects.filter(
            Q(product__category=self.object) |
            Q(product__category__parent=self.object) |
            Q(product__category__parent__parent=self.object) |
            Q(product__category__parent__parent__parent=self.object)
        ).distinct()
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

        try:
            offer = Offer.objects.get(id=offer_id)
        except Offer.DoesNotExist:
            raise Http404

        click = Click.objects.make(offer=offer,
                                   user_ip=self.request.META.get('REMOTE_ADDR'))
        user = offer.shop.user

        try:
            balance = user.client_profile.balance
        except:
            balance = Balance.objects.make(client=user.client_profile)

        BalanceHistory.objects.decrease(
            balance=balance,
            click=click,
            value=offer.click_price)

        return offer.url


class CategoryStatisticsView(TemplateView):
    template_name = "apps/catalog/category_statistics.html"

    def extract_get_args(self):
        date_from = self.request.GET.get('date_from', None)
        date_to = self.request.GET.get('date_to', None)

        date_from = datetime.strptime(date_from, '%d.%m.%y').date() if date_from else None
        date_to = datetime.strptime(date_to, '%d.%m.%y').date() if date_to else date.today()

        if not date_from:
            date_from = CategoryStatistics.objects.all().order_by('created').first().created

        return date_from, date_to

    def get_category_list(self):
        search = self.request.GET.get('search', None)
        category_list = Category.objects.all()

        if search:
            category_list = category_list.filter(name__icontains=search)

        return category_list

    def get_context_data(self, **kwargs):
        context = super(CategoryStatisticsView, self).get_context_data()
        date_from, date_to = self.extract_get_args()
        category_list = self.get_category_list()

        object_list = list()
        for category in category_list:
            try:
                start_statistics = CategoryStatistics.objects.get(created=date_from,
                                                                  category=category)
                end_statistics = CategoryStatistics.objects.get(created=date_to,
                                                                category=category)
            except CategoryStatistics.DoesNotExist:
                continue

            shop_list = Shop.objects.filter(offer__product__category=category).distinct()

            object_list.append({
                "name": start_statistics.category.name,
                "level": start_statistics.category.depth,
                "click_count": end_statistics.click_count - start_statistics.click_count,
                "product_count": end_statistics.product_count - start_statistics.product_count,
                "shop_count": end_statistics.shop_count - start_statistics.shop_count,
                "shop_list": shop_list
            })

        context["object_list"] = object_list
        return context