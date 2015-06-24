import urllib
import xmltodict
from django.conf import settings
from django.core.validators import EMPTY_VALUES
from django.utils.translation import ugettext_lazy as _
from django.db import models
# Project imports
from catalog.models import Category, Currency
from product import models as productmodels
from .shop import Shop


class MakeException(Exception):
    # 'https://yandex.st/market-export/1.0-17/partner/help/YML.xml'
    ""


class ShopYMLManager(models.Manager):
    def get_data(self, data):
        if data in EMPTY_VALUES:
            raise MakeException('Empty yml')

        catalog = data.get('yml_catalog', None)
        if catalog in EMPTY_VALUES:
            raise MakeException('no yml_catalog in file')
        shop = catalog.get('shop', None)
        if shop in EMPTY_VALUES:
            raise MakeException('no shop in file')
        offers = shop.get('offers', None)
        offers = offers.get('offer', None)

        if offers in EMPTY_VALUES:
            raise MakeException('no offers')
        if not len(offers) > 0:
            raise MakeException('no offers')

        categories = shop.get('categories', None)
        categories = categories.get('category', None)
        currency = shop.get('currencies').get('currency')
        return categories, currency, offers

    def make(self, shop, yml):
        if not isinstance(shop, Shop):
            raise MakeException(_('invalid shop object'))
        # TODO: check - shop is active
        data = None
        try:
            obj = self.model()
            obj.shop = shop
            obj.yml_url = yml
            data = obj.parse_yml()

        except:
            raise MakeException('invalid yml url')

        categories, currency, offers = self.get_data(data)

        # Search currency in catalog.Currency or create it
        obj.currency = Currency.objects.make(codename=currency.get('@id'))

        # Append catalog.Category object to every row with key 'system_cat'
        # If it does not exists,
        # Category.objects.make_from_yml method will create it
        for c in categories:
            c.update({'system_cat': Category.objects.make_from_yml(c)})

        obj.save()
        # create OfferCategories rows
        offercats = OfferCategories.objects.make_from_parsed_list(shopyml=obj,
                                                                  plist=categories)

        for offer in offers:
            product = productmodels.Product.objects.make_from_yml(offer)

            productshop = productmodels.ProductShop.objects.make_from_yml(
                product=product,
                shop=shop,
                currency=currency,
                yml_obj=offer,
                offercats=offercats)

            productmodels.ProductShopDelivery.objects.make_from_yml(
                productshop=productshop,
                yml_obj=offer)
        return obj


class ShopYML(models.Model):
    shop = models.ForeignKey(Shop,
                             verbose_name=_('Магазин'))
    yml_url = models.URLField(verbose_name=_('YMl url'))
    created = models.DateTimeField(auto_now_add=True,
                                   editable=False,
                                   verbose_name=_(u'Дата создания'))
    currency = models.ForeignKey(Currency,
                                 default=None,
                                 null=True,
                                 blank=True,
                                 verbose_name=_('Валюта'))

    objects = ShopYMLManager()

    def parse_yml(self):
        yml_file = urllib.request.urlopen(self.yml_url)
        data = yml_file.read()
        yml_file.close()
        return xmltodict.parse(data)

    class Meta:
        verbose_name = _('YML файл магазина')
        verbose_name_plural = _('YML файлы магазинов')


class OfferCategoriesManager(models.Manager):
    def make_from_parsed_list(self, plist, shopyml):
        offercats = list()
        for cats in plist:
            offercats.append(
                self.model(category=cats.get('system_cat'), shopyml=shopyml))
        if len(offercats) > 0:
            self.bulk_create(offercats)
            return offercats
        else:
            return None


class OfferCategories(models.Model):
    shopyml = models.ForeignKey(ShopYML,
                                verbose_name=_('Предложение'))
    category = models.ForeignKey(Category,
                                 verbose_name=_('Категория'))
    price = models.IntegerField(null=True,
                                blank=True,
                                default=settings.DEFAULT_CLICK_PRICE,
                                verbose_name=_('Цена за клик'))

    objects = OfferCategoriesManager()

    class Meta:
        verbose_name = _('Категории предложения')
        verbose_name_plural = _('Категории предложений')
