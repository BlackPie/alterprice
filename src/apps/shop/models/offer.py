import urllib
import xmltodict
from django.conf import settings
from django.core.validators import EMPTY_VALUES
from django.utils.translation import ugettext_lazy as _
from django.db import models

from catalog.models.category import Category
from catalog.models.city import City
from catalog.models.currency import Currency
from utils.abstract_models import PublishModel
from product import models as productmodels
from .shop import Shop


class MakeException(Exception):
    # 'https://yandex.st/market-export/1.0-17/partner/help/YML.xml'
    ""


class PricelistManager(models.Manager):
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

    def make(self, shop, yml, region, name=None):
        if not isinstance(shop, Shop):
            raise MakeException(_('invalid shop object'))
        # TODO: check - shop is active
        data = None
        try:
            obj = self.model()
            obj.shop = shop
            obj.yml_url = yml
            obj.region = region
            if not name:
                name = 'Прайс-лист #%d' % shop.id
            obj.name = name
            data = obj.parse_yml()

        except:
            raise MakeException('invalid yml url')

        categories, currency, offers = self.get_data(data)

        # Search currency in catalog.Currency or create it
        if isinstance(currency, list):
            try:
                cur = Currency.objects.make(codename=currency[0].get('@id'))
            except:
                cur = Currency.objects.first()
        else:
            cur = Currency.objects.make(codename=currency.get('@id'))
        obj.currency = cur

        # Append catalog.Category object to every row with key 'system_cat'
        # If it does not exists,
        # Category.objects.make_from_yml method will create it
        for c in categories:
            c.update({'system_cat': Category.objects.make_from_yml(c)})

        obj.save()
        # create OfferCategories rows
        offercats = OfferCategories.objects.make_from_parsed_list(pricelist=obj,
                                                                  plist=categories)

        for offer in offers:
            product = productmodels.Product.objects.make_from_yml(offer)

            productshop = productmodels.Offer.objects.make_from_yml(
                pricelist=obj,
                product=product,
                shop=shop,
                currency=obj.currency,
                yml_obj=offer,
                offercats=offercats)

            productmodels.OfferDelivery.objects.make_from_yml(
                productshop=productshop,
                yml_obj=offer)
        return obj


class Pricelist(PublishModel):
    NEW = 1
    PROCESSED = 2
    CANT_PROCESS = 3
    STATUS_CHOICES = (
        (NEW, "Новый"),
        (PROCESSED, "Обработан"),
        (CANT_PROCESS, "Невозможно обработать"),
    )
    status = models.IntegerField(default=NEW, choices=STATUS_CHOICES)
    shop = models.ForeignKey(Shop,
                             verbose_name=_('Магазин'))
    name = models.CharField(max_length=255,
                            verbose_name=_('Название'))
    yml_url = models.URLField(verbose_name=_('YMl url'))
    created = models.DateTimeField(auto_now_add=True,
                                   editable=False,
                                   verbose_name=_(u'Дата создания'))
    currency = models.ForeignKey(Currency,
                                 default=None,
                                 null=True,
                                 blank=True,
                                 verbose_name=_('Валюта'))
    region = models.ForeignKey(City)
    objects = PricelistManager()

    def parse_yml(self):
        yml_file = urllib.request.urlopen(self.yml_url)
        data = yml_file.read()
        yml_file.close()
        return xmltodict.parse(data)

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = _('Прайс лист магазина')
        verbose_name_plural = _('Прайс листы магазинов')


class OfferCategoriesManager(models.Manager):
    def make_from_parsed_list(self, plist, pricelist):
        offercats = list()
        for cats in plist:
            offercats.append(
                self.model(category=cats.get('system_cat'), pricelist=pricelist))
        if len(offercats) > 0:
            self.bulk_create(offercats)
            return self.filter(pricelist=pricelist)
        else:
            return None


class OfferCategories(models.Model):
    pricelist = models.ForeignKey(Pricelist,
                                verbose_name=_('Прайс лист'))
    category = models.ForeignKey(Category,
                                 verbose_name=_('Категория'))
    price = models.IntegerField(null=True,
                                blank=True,
                                default=settings.DEFAULT_CLICK_PRICE,
                                verbose_name=_('Цена за клик'))

    objects = OfferCategoriesManager()

    def __str__(self):
        return "%d %s" % (self.pk, self.category.name)

    def __unicode__(self):
        return "%d %s" % (self.pk, self.category.name)

    class Meta:
        verbose_name = _('Категории предложения')
        verbose_name_plural = _('Категории предложений')
