from catalog.models.category import Category
from catalog.models.city import City


def categories(request):
    return {'categories': Category.objects.get_frist_level()}


def current_url(request):
    return {'current_url': request.get_full_path()}


def cities(request):
    return {'cities': City.objects.all()}


def current_city(request):
    return {'current_city': City.objects.filter(
        id=request.session.get('city_id')).first()}
