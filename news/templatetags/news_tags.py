from django import template
from news.models import Category
from django.db.models import Count
register = template.Library()
@register.simple_tag()
def get_categories():
    return Category.objects.all()

@register.inclusion_tag('news/list_categories.html')
def show_categories():
    #categories = Category.objects.all()
    filtr = Category.objects.filter(news__is_published=True)
    categories = filtr.annotate(cnt=Count('news'))

    return {'categories':categories,}