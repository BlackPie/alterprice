from ipware.ip import get_ip
from django_geoip.models import IpRange
from catalog.models.city import City


MSC = 'Москва'
SP = 'Санкт-Петербург'


class CityMiddleware(object):
    def process_request(self, request):
        city_id = request.session.get('city_id', None)

        if not city_id:
            ip = get_ip(request)

            try:
                city_name = IpRange.objects.by_ip(ip).city.name
            except IpRange.DoesNotExist:
                city_name = None

            if city_name:
                if city_name not in (MSC, SP):
                    city_id = City.objects.get(default_city=True).id
                else:
                    try:
                        city_id = City.objects.get(name=city_name).id
                    except City.DoesNotExist:
                        city_id = None
            else:
                city_id = None

            request.session['city_id'] = city_id
