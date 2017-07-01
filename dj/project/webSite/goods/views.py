# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, render_to_response,redirect

# Create your views here.
def mainPage(request):
    return render_to_response("base.html")