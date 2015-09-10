from django.views.generic import TemplateView
from catalog.models.category import Category


class IndexView(TemplateView):
    template_name = 'apps/index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['constructors'] = Category.objects.filter(name__icontains='конструкторы').first()
        context['notebooks'] = Category.objects.filter(name__icontains='ноутбуки').first()
        context['tablets'] = Category.objects.filter(name__icontains='планшеты').first()
        context['tvs'] = Category.objects.filter(name__icontains='телевизоры').first()
        context['toys'] = Category.objects.filter(name__icontains='мягкие игрушки').first()
        context['phones'] = Category.objects.filter(name__icontains='телефоны').first()
        context['headphones'] = Category.objects.filter(name__icontains='наушники').first()
        context['babymonitors'] = Category.objects.filter(name__icontains='видеонhяни').first()
        return context