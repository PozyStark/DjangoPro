from django import template
from substation.models import *

register = template.Library()


@register.simple_tag(name='get_cats')
def get_categories(filter_arg=None):
    if not filter_arg:
        return Category.objects.all()
    else:
        return Category.objects.filter(pk=filter_arg)


@register.inclusion_tag('substation/list_categories.html')
def show_categories(sort=None, cat_selected=0):
    if not sort:
        cats = Category.objects.all()
    else:
        cats = Category.objects.order_by(sort)

    return {'cats': cats, 'cat_selected': cat_selected}


@register.inclusion_tag('substation/menu_items.html')
def show_menu_items():
    menu = [
        {'title': "О сайте", 'url_name': 'about'},
        {'title': "Добавить статью", 'url_name': 'add_page'},
        {'title': "Обратная связь", 'url_name': 'contact'},
        {'title': "Войти", 'url_name': 'login'}
    ]
    return {'menu': menu}