import random
from django.core.management.base import BaseCommand
from apuser.models import AlterPriceUser, ClientProfile
from brand.models import Brand
from catalog.models.category import Category
from shop import models as shopmodels
from product import models as productmodels
from catalog import models as catalogmodels


# class Command(BaseCommand):
#     def handle(self, *args, **options):
#         users = list()
#         brands = list()
#         categories = list()
#         shops = list()
#         clients = list()
#         products = list()
#         productshops = list()
#         properties = list()
#         deliveris = list()
#
#         for x in range(1, 10):
#             b = Brand()
#             b.name = 'Brand_%d' % x
#             brands.append(b)
#
#             u = AlterPriceUser()
#             u.email = 'email_%d@example.com' % x
#             u.set_password('123')
#             users.append(u)
#
#             c = Category()
#             c.name = 'Category_%d' % x
#             categories.append(c)
#
#         AlterPriceUser.objects.bulk_create(users)
#         Brand.objects.bulk_create(brands)
#         Category.objects.bulk_create(categories)
#
#         for u in AlterPriceUser.objects.all():
#             c = ClientProfile()
#             c.user = u
#             c.name = 'Client %d' % u.id
#             clients.append(c)
#
#             s = shopmodels.Shop()
#             s.user = u
#             s.name = 'Shop %d' % u.id
#             s.ogrn = '0000%d' % u.id
#             s.entity = 'LLC %s' % s.name
#             shops.append(s)
#
#         ClientProfile.objects.bulk_create(clients)
#         shopmodels.Shop.objects.bulk_create(shops)
#         shops = shopmodels.Shop.objects.all()
#
#         for b in Brand.objects.all():
#             p = productmodels.Product()
#             p.name = 'Product_%d' % b.id
#             p.brand = b
#             p.description = 'Description %s' % b.id
#             products.append(p)
#
#         productmodels.Product.objects.bulk_create(products)
#
#         for p in productmodels.Product.objects.all():
#             for x in range(0, 3):
#                 ps = productmodels.Offer()
#                 ps.product = p
#                 ps.price = random.randrange(100, 10000)
#                 ps.shop = random.choice(shops)
#                 productshops.append(ps)
#
#                 prop = productmodels.ProductProperty()
#                 prop.product = p
#                 prop.name = 'Property_%d_%s' % (p.id, x)
#                 properties.append(prop)
#
#         productmodels.Offer.objects.bulk_create(productshops)
#         productmodels.ProductProperty.objects.bulk_create(properties)
#
#         # for prop in productmodels.ProductProperty.objects.all():
#         #     for x in range(0, 3):
#         #         pi = productmodels.PropertyInfo()
#         #         pi.productproperty = prop
#         #         pi.property_name = 'prop_name_%d_%d' % (prop.id, x)
#         #         pi.property_value = 'prop_value_%d_%d' % (prop.id, x)
#         #         prop_infos.append(pi)
#         # productmodels.PropertyInfo.objects.bulk_create(prop_infos)
#
#         for ps in productmodels.Offer.objects.all():
#             d = productmodels.OfferDelivery()
#             d.productshop = ps
#             d.pickup = random.choice((True, False))
#             d.delivery = random.choice((True, False))
#             d.price = random.randrange(110, 1000)
#             deliveris.append(d)
#         productmodels.OfferDelivery.objects.bulk_create(deliveris)
#
#         admin = AlterPriceUser()
#         admin.email = 'admin@admin.com'
#         admin.is_staff = True
#         admin.is_superuser = True
#         admin.set_password('123')
#         admin.save()
