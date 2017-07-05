from django.conf.urls import url,include
from django.contrib import admin
# -*- coding: utf-8 -*-
from .views import *

urlpatterns = [

    url(r'^$', profile, name='profile'),
    url(r'^login/$', LogIn,name='LogIn'),
    url(r'^logout/$', LogOut,name='LogOut'),
    url(r'^registration/$',registr,name="registration")
]
