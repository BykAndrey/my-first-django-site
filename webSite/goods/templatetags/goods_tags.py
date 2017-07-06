from distutils.command import register
from django import template
from django.template.defaultfilters import stringfilter
from  django.core.urlresolvers import reverse
from goods.models import Category,Product
from goods.views import *
register = template.Library()


from imagekit import ImageSpec,register as reg
from imagekit.processors import ResizeToFill

class Thumbnail(ImageSpec):
    processors = [ResizeToFill(100, 50)]
    format = 'JPEG'
    options = {'quality': 60}

reg.generator('goods:thumbnail', Thumbnail)

@register.inclusion_tag('header.html')
def header(request):
    return {"request":request}

@register.inclusion_tag('SideMenu/LinkCategory.html')
def linkcategory(t):
    cats=Category.objects.filter(topcategory=t, published=True)
    return {'category':cats}


@register.inclusion_tag('side_menu.html')
def side_menu():
    topcats=Topcategory.objects.filter(published=True)
    return {'topcategory':topcats}

@register.inclusion_tag('temp_tag_good.html')
def tag_good(good):

    #cats = WholeUrl(good)
    #good.url=reverse('cardgood',args={cats:u'urlcat',good.url:u'urlgood'})
    return {'good':good}

