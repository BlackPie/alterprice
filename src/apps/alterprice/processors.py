from catalog.models import Category, City


def categories(request):
    return {'categories': Category.objects.get_frist_level()}


def current_url(request):
    return {'current_url': request.get_full_path()}


def cities(request):
    return {'cities': City.objects.all()}
