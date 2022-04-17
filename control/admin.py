from django.contrib import admin
from .models import *


# Register your models here.
class Category_Admin(admin.ModelAdmin):
    list_display = ['pk', 'category', 'slug']


class SubCategory_Admin(admin.ModelAdmin):
    list_display = ['pk', 'sub_category', 'slug', 'category_slug']
    list_filter = ['category_slug']


class Product_Admin(admin.ModelAdmin):
    list_display = ['pk', 'name', 'slug', 'price', 'subcategory_slug', 'category_slug', 'on_main']
    list_filter = ['category_slug', 'subcategory_slug', 'on_main']


class Apply_Admin(admin.ModelAdmin):
    list_display = ['applier_name', 'applier_phone', 'message', 'date_applied']
    list_filter = ['applier_phone']


class Service_Admin(admin.ModelAdmin):
    list_display = ['name', 'on_main']
    list_filter = ['on_main']


class News_Admin(admin.ModelAdmin):
    list_display = ['pk', 'title', 'date', 'on_main']
    list_filter = ['title', 'on_main']


admin.site.register(Category, Category_Admin)
admin.site.register(SubCategory, SubCategory_Admin)
admin.site.register(Product, Product_Admin)
admin.site.register(Apply, Apply_Admin)
admin.site.register(Service, Service_Admin)
admin.site.register(News, News_Admin)

