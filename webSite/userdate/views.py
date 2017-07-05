# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.models import User
from django.shortcuts import render_to_response, redirect,render
from django.template.context_processors import csrf

from .forms import *

from .models import UserInformations
# Create your views here.


def profile(request):
    args={}
    args.update(csrf(request))
    user=User.objects.get(username=request.user.username)
    args['email'] = user.email
    args['fname'] = user.first_name
    args['lname'] = user.last_name

    return render(request,"profile.html",args)

def LogIn(request):
    args = {}
    args.update(csrf(request))

    if request.user.is_authenticated:

        return render_to_response("home.html",args)

    logout(request)
    if request.method=="POST":
        form=LoginForm(request.POST)
        if form.is_valid():
            user=authenticate(username=form.cleaned_data['email'],password=form.cleaned_data['password'])
            if user is not None:
                if user.is_active:
                    login(request,user)
                else:
                    args['error'] = "Данный пользователь не активен"
                return redirect("/")
            else:
                args['error']="Проверте правильность введенных данных"
                args['form'] = form
                return render(request, "login.html",args)
    else:
        form= LoginForm()
    args['form'] = form

    return render(request, "login.html", args)

def LogOut(request):
    logout(request)
    return render(request, "home.html")



def registr(request):
    if request.user.is_authenticated:
        return redirect('/')
    args = {}
    args.update(csrf(request))
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            lastname = form.cleaned_data['lastname']
            phonenumber = form.cleaned_data['phonenumber']
            user = User.objects.create_user(email, email, password)
            user.first_name = name
            user.last_name = lastname
            user.save()
            userInfo = UserInformations.objects.create(
                userId=user,
                name=name,
                lastname=lastname,
                phonenumber=phonenumber,
                email=email)
            userInfo.save()

            if user:
                return redirect('/')


    else:
        form = RegistrationForm()
    args['form'] = form
    return render(request, "registration.html", args)