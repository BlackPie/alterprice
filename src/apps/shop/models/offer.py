import urllib
from django.dispatch import receiver
import xmltodict
from django.conf import settings
from django.core.validators import EMPTY_VALUES
from django.utils.translation import ugettext_lazy as _
from django.db import models
from apuser.models.profile import EmailDelivery

from catalog.models.category import Category
from catalog.models.city import City
from catalog.models.currency import Currency
from django.db.models.signals import post_save, pre_save
from utils.abstract_models import PublishModel
from product import models as productmodels
from .shop import Shop
from product.models.other import Offer


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

    def make(self, shop, region, name, yml_url):
        obj = self.model(
            shop=shop,
            name=name,
            yml_url=yml_url,
            region=region,
        )
        obj.save()
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


@receiver(pre_save, sender=Pricelist)
def pricelist_change_pre_callback(sender, instance, **kwargs):
    instance._status_old = instance.status
    instance._publish_status_old = instance.publish_status

@receiver(post_save, sender=Pricelist)
def pricelist_change_callback(sender, instance, **kwargs):
    if instance.shop.user.client_profile.operator:
        if instance._status_old != instance.status:
            EmailDelivery.objects.make(
                template='operator/pricelist_status.html',
                email=instance.shop.user.client_profile.operator.user.email,
                context={'status': instance.status},
            )
        if instance._publish_status_old != instance.publish_status:
            EmailDelivery.objects.make(
                template='operator/pricelist_status.html',
                email=instance.shop.user.client_profile.operator.user.email,
                context={'status': instance.publish_status},
            )

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

    def get_or_create(self, pricelist, category):
        try:
            offer_category = self.model.objects.get(category=category,
                                                    pricelist=pricelist)
        except OfferCategories.DoesNotExist:
            offer_category = self.model.objects.create(category=category,
                                                       pricelist=pricelist)
        return offer_category


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

    def save(self, *args, **kwargs):
        offer_list = Offer.objects.filter(offercategory=self)

        for offer in offer_list:
            offer.click_price = self.price
            offer.save()

        super(OfferCategories, self).save(*args, **kwargs)

    class Meta:
        verbose_name = _('Категории предложения')
        verbose_name_plural = _('Категории предложений')
