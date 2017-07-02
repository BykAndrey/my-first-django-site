# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import *
from django.forms import TextInput, ModelForm, Textarea, Select
# Register your models here.


class ProductFilterForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(ProductFilterForm, self).__init__(*args, **kwargs)
        if self.instance:
            i = self.instance
            if i.filtercat:
                self.fields['value'].queryset = FilterSelect.objects.filter(filtercategory=self.instance.filtercat)

    class Meta:
        model = ProductFilter
        fields = '__all__'


class FilterSelectInline(admin.TabularInline):
    model = FilterSelect
    extra = 1


class FilterCategoryAdmin(admin.ModelAdmin):
    inlines = [FilterSelectInline]


class ProductFilterInline(admin.TabularInline):
    model = ProductFilter
    extra = 1
    form = ProductFilterForm


class FilterCategoryInline(admin.TabularInline):
    model = FilterCategory
    extra = 1


class CategoryPropertyInline(admin.TabularInline):
    extra = 3
    model = CategoryProperty


class ProductPropertyInline(admin.TabularInline):
    extra = 3
    model = ProductProprty



class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name','dateCreated','dateUpdate']
    fields = ['topcategory','published','name','description','url']
    inlines = [CategoryPropertyInline,FilterCategoryInline]


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'dateCreated', 'dateUpdate']
    fields = ['published','category','name','url','images','description','price','is_hit','is_new']
    inlines = [ProductPropertyInline,ProductFilterInline]

class topclassAdmin(admin.ModelAdmin):
    list_display = ['name', 'dateCreated', 'dateUpdate']
    fields = ['name','published', 'description', 'url']
admin.site.register(Topcategory, topclassAdmin)
admin.site.register(Product,ProductAdmin)
admin.site.register(Category,CategoryAdmin)
admin.site.register(FilterCategory,FilterCategoryAdmin)