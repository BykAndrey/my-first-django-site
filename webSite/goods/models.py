# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import uuid


from django.db import models

# Create your models here.


from django.utils.encoding import python_2_unicode_compatible

from webSite import settings


def make_upload_path(instance, filename, prefix = False):
    """
    Create unique name for image or file.
    """
    new_name = str(uuid.uuid1())
    parts = filename.split('.')
    f = parts[-1]
    filename = new_name + '.' + f
    return u"%s/%s" % ("images/", filename)

class commonInfo(models.Model):
    dateCreated = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата создания"
    )
    dateUpdate = models.DateTimeField(
        auto_now=True,
        verbose_name="Дата обнавления"
    )

    class Meta:
        abstract = True


class OrderingBaseModel(commonInfo):
    published = models.BooleanField(default=True)
    description = models.TextField(default="")
    url=models.CharField(default="-",max_length=150)

    class Meta:
        abstract = True

@python_2_unicode_compatible
class Topcategory(OrderingBaseModel):
    class Meta():
        verbose_name_plural = "Категории"
        verbose_name="Категория"
    name = models.CharField(max_length=150, verbose_name="Категория", default="")
    def __str__(self):
        return self.name

@python_2_unicode_compatible
class Category(OrderingBaseModel):
    class Meta():
        verbose_name_plural = "Подкатегории"
        verbose_name="Подкатегория"
    topcategory=models.ForeignKey(Topcategory,blank=True,on_delete=models.CASCADE,null=True)
    name = models.CharField(max_length=150, verbose_name="Подкатегория", default="")

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class Product(OrderingBaseModel):
    class Meta():
        verbose_name_plural = "Товары"
        verbose_name="Товар"
    name = models.CharField(max_length=150, verbose_name="Продукт", default="")
    category = models.ForeignKey(Category)
    price=models.IntegerField(default=0,verbose_name="Цена", blank=False)
    is_hit=models.BooleanField(default=False,verbose_name="Хит")
    is_new = models.BooleanField(default=False,verbose_name="Новинка")
    images=models.ImageField(null=True, blank=True,upload_to=make_upload_path,verbose_name="Изображение")
    def save(self, *args, **kwargs):
        if self.category:
            super(Product, self).save(*args, **kwargs)


            for cat in CategoryProperty.objects.filter(category=self.category):
                pp = ProductProprty.objects.filter(categoryprop=cat, product=self)
                if not pp:
                    ProductProprty.objects.create(categoryprop=cat, product=self)

            for catf in FilterCategory.objects.filter(category_id=self.category):
                pf = ProductFilter.objects.filter(filtercat=catf, product_id=self)
                if not pf:
                    ProductFilter.objects.create(filtercat=catf, product_id=self)


    def __str__(self):
        return self.name




@python_2_unicode_compatible
class CategoryProperty(commonInfo):
    category = models.ForeignKey(Category)
    name = models.CharField(max_length=50, verbose_name="Название", default="")

    def __str__(self):  # __unicode__ on Python 2
        return self.name


class ProductProprty(commonInfo):
    categoryprop = models.ForeignKey(CategoryProperty)
    value = models.CharField(default="", max_length=50, verbose_name="Значение")
    product = models.ForeignKey(Product)


@python_2_unicode_compatible
class FilterCategory(commonInfo):
    class Meta():
        verbose_name_plural="Фильтры категории"
        verbose_name="Фильтр категории"
    category_id = models.ForeignKey(Category)
    name = models.CharField(default="", max_length=50)

    def __str__(self):  # __unicode__ on Python 2
        return self.name


@python_2_unicode_compatible
class FilterSelect(commonInfo):
    filtercategory = models.ForeignKey(FilterCategory)
    name = models.CharField(max_length=10, default="")

    def __str__(self):  # __unicode__ on Python 2
        return self.name


class ProductFilter(commonInfo):
    filtercat = models.ForeignKey(FilterCategory,
                                  on_delete=models.CASCADE,
                                  null=True,
                                  related_name='filter_select_product'                                  )
    product_id = models.ForeignKey(Product)
    value = models.ManyToManyField(FilterSelect,  related_name='filtervalues',
blank=True)
    def __str__(self):
        return str(self.id)
