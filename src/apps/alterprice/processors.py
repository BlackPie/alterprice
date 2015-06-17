from catalog.models import Category


def categories(request):
    return {'categories': Category.objects.get_frist_level()}


def current_url(request):
    return {'current_url': request.get_full_path()}
