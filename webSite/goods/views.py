# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, render_to_response,redirect
from .models import *
# Create your views here.
def WholeUrl(obj):
    caturl=Category.objects.filter(id=obj.category.id)[0].url
    return caturl+"/"+obj.url

def mainPage(request):
    args={}
    goods=Product.objects.filter(is_new=True,published=True)
    for ob in goods:


        ob.url=WholeUrl(ob)

    args["goods"]=goods
    return render_to_response("home.html",args)
    #="kirpichi" ="pechnoi"
def cardGood(request,urlcat,urlgood):
    args = {}
    cat = Category.objects.filter(url=urlcat)[0]
    if cat:
        args["good"]=Product.objects.filter(url=urlgood,published=True)[0]

    return render_to_response("cardGood.html", args)

