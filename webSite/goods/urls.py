"""webSite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
# -*- coding: utf-8 -*-
from django.conf import settings
from django.conf.urls import *
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from .views import *
urlpatterns =[


    url(r'^category/(?P<url>\w+)/$', topcategory,name='topcategory'),
    url(r'^category/(?P<url>\w+)/(?P<idtop>\w+)/$', category,name='category'),
    url(r'^card/(?P<urlcat>\w+)/(?P<urlgood>\w+)/$', cardGood,name='cardgood'),
    url(r'^cart/$',cart,name='cart'),

    url(r'^$',mainPage),

]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
