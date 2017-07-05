# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import auth
from django.contrib.auth.models import User
from django import http
from django.http import Http404
from django.shortcuts import render, render_to_response,redirect
from django.template import RequestContext

from .models import *
# Create your views here.
def WholeUrl(obj):
    caturl=Category.objects.filter(id=obj.category.id)[0].url
    return caturl
def custom_proc(request):
    return {
        'app': 'My app',
        'user': request.user,
        'ip_address': request.META['REMOTE_ADDR']
    }

def mainPage(request):
    args={}
    print(request.user.username)
    args['authenticated'] = request.user.is_authenticated()
    if args['authenticated'] == True:
        args['username'] = request.user.username
    args["goods"]=Product.objects.filter(is_new=True,published=True)
    return render(request, 'home.html', args)
   # return render_to_response("home.html",args,        context_instance=RequestContext(request, processors=[custom_proc]))
    #="kirpichi" ="pechnoi"


#Корзина
def cart(request):
    args={}
    args['authenticated'] = request.user.is_authenticated()
    if args['authenticated'] == True:
        args['username'] = request.user.username
    return render(request, 'cartPage.html', args)
    #return render_to_response("cartPage.html",args,        context_instance=RequestContext(request, processors=[custom_proc]))

def topcategory(request, url):
    args = {}
    args['authenticated'] = request.user.is_authenticated()
    if args['authenticated'] == True:
        args['username'] = request.user.username
    cat = Topcategory.objects.filter(url=url,published=True)[0]
    if cat:
        cats=Category.objects.filter(topcategory=cat,published=True)
        args["goods"]=[]
        for ct in cats:
            args["goods"].extend(Product.objects.filter(category_id=ct,published=True))
        args['name_cat']= cat.name
    else:
        raise Http404("Error")
    return render(request, 'top_category_list.html', args)
    #return render_to_response("top_category_list.html", args,        context_instance=RequestContext(request, processors=[custom_proc]))


def category(request, url,idtop):
    args={}
    args['authenticated'] = request.user.is_authenticated()
    if args['authenticated'] == True:
        args['username'] = request.user.username
    cat=Category.objects.filter(url=url,published=True)[0]
    if cat:
        args["goods"]=Product.objects.filter(category_id=cat,published=True)
    if cat:
        args['name_cat'] = cat.name
    return render(request, 'category.html', args)
    #return render_to_response("category.html", args,context_instance=RequestContext(request, processors=[custom_proc]))

def cardGood(request,urlcat,urlgood):
    args = {}
    args['authenticated'] = request.user.is_authenticated()
    if args['authenticated'] == True:
        args['username'] = request.user.username
    cat = Category.objects.filter(url=urlcat,published=True)[0]
    if cat:

        args["good"]=Product.objects.filter(url=urlgood,published=True)[0]
    return render(request, 'cardGood.html', args)
    #return render_to_response("cardGood.html", args,context_instance=RequestContext(request, processors=[custom_proc]))

