# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from django.contrib.auth.models import User
# Create your models here.
from django.utils.encoding import python_2_unicode_compatible
@python_2_unicode_compatible
class UserInformations(models.Model):
    class Meta():
        verbose_name="Информация о пользователе"
    userId=models.ForeignKey(User)
    name=models.CharField(max_length=25,verbose_name="Имя")
    lastname=models.CharField(max_length=25,verbose_name="Фамилия")
    phonenumber=models.CharField(max_length=13,verbose_name="Телефон")
    email=models.EmailField(verbose_name="Email")

    def __str__(self):
        return self.email +" "+self.lastname
