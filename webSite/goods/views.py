# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import Http404
from django.shortcuts import render, render_to_response,redirect
from .models import *
# Create your views here.
def WholeUrl(obj):
    caturl=Category.objects.filter(id=obj.category.id)[0].url
    return caturl

def mainPage(request):
    args={}

    args["goods"]=Product.objects.filter(is_new=True,published=True)
    return render_to_response("home.html",args)
    #="kirpichi" ="pechnoi"




def topcategory(request, url):
    args = {}
    cat = Topcategory.objects.filter(url=url,published=True)[0]
    if cat:
        cats=Category.objects.filter(topcategory=cat,published=True)
        args["goods"]=[]
        for ct in cats:
            args["goods"].extend(Product.objects.filter(category_id=ct,published=True))
        args['name_cat']= cat.name
    else:
        raise Http404("Error")
    return render_to_response("top_category_list.html", args)


def category(request, url,idtop):
    args={}
    cat=Category.objects.filter(url=url,published=True)[0]
    if cat:
        args["goods"]=Product.objects.filter(category_id=cat,published=True)
    if cat:
        args['name_cat'] = cat.name
    return render_to_response("category.html", args)

def cardGood(request,urlcat,urlgood):
    args = {}
    cat = Category.objects.filter(url=urlcat,published=True)[0]
    if cat:

        args["good"]=Product.objects.filter(url=urlgood,published=True)[0]

    return render_to_response("cardGood.html", args)

