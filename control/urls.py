from django.template.context_processors import request
from django.urls import path
from .views import *


urlpatterns = [
    path('', index_view, name="home"),
    path('products/', all_products_view, name="products"),
    path('products/<slug:category_slug>', category_products_view, name="category_products"),
    path('products/<slug:category_slug>/<slug:subcategory_slug>/', subcategory_products_view,
         name="subcategory_products"),
    path('services/', services_view, name="services"),
    path('news/', news_view, name="news"),
    path('about_company/', company_view, name="about_company"),
    path('projects/', company_view, name="projects"),
    path('contacts/', contacts_view, name="contacts"),
    # path('item-detail/<slug:slug>/<int:pk>/', detail_view, name="item-detail"),
    path('item-detail/<slug:slug>/<int:pk>/', detail_view, name="item-detail"),
]
