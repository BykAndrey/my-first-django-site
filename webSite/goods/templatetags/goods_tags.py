from distutils.command import register
from django import template
from goods.models import Category
register = template.Library()

@register.inclusion_tag('side_menu.html')
def side_menu():
    cats=Category.objects.filter(published=True)
    return {'category':cats}

@register.inclusion_tag('temp_tag_good.html')
def tag_good(good):
    return {'good':good}
