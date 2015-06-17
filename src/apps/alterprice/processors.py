from catalog.models import Category


def categories(request):
    return {'categories': Category.objects.get_frist_level()}
