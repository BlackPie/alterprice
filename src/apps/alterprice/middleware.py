from catalog.models.city import City


class CityMiddleware(object):
    def process_request(self, request):
        if 'city_id' not in request.session.keys():
            city = City.objects.first()
            if city:
                request.session['city_id'] = city.id
