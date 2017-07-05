# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import UserInformations
from django.contrib import admin

# Register your models here.
class UserInformationsAdmin(admin.ModelAdmin):
    exclude = ['userId']
admin.site.register(UserInformations,UserInformationsAdmin)