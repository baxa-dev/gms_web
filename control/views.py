from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
from .models import *
from .forms import *
from config import settings
import requests


# Create your views here.
def index_view(request):
    # products = Product.objects.all()
    # services = Service.objects.all()
    # news = News.objects.all()
    # context = {'products': products, 'services': services, 'news': news}
    if request.method == "POST":
        form_data = ApplyForm(request.POST)
        name = request.POST.get('applier_name')
        phone = request.POST.get('applier_phone')
        message = request.POST.get('message')
        if form_data.is_valid():
            form_data.applier_name = name
            form_data.applier_phone = phone
            form_data.message = message
            form_data.save()
        requests.get(f"http://api.telegram.org/bot{settings.TOKEN}/sendMessage?chat_id={settings.CHANNEL_ID}&text=Поступила заявка :\n\n"
                     f"Имя :  {name}\nНомер телефона :  {phone}\nСообщение :  {message}")
        return HttpResponseRedirect(request.path)
    else:
        products = Product.objects.all()
        services = Service.objects.all()
        news = News.objects.all()
        context = {'products': products, 'services': services, 'news': news}
        return render(request=request, template_name='index.html', context=context)


def subcategory_products_view(request, category_slug, subcategory_slug):
    # category = request.GET.get("category")
    # sub_category = request.GET.get("sub_category")
    categories = Category.objects.all()
    sub_categories = SubCategory.objects.filter(category_slug__slug=category_slug)
    products = Product.objects.filter(subcategory_slug__slug=subcategory_slug)

    page_num = request.GET.get("page")
    paginator = Paginator(products, 4)
    page_obj = paginator.get_page(page_num)

    try:
        products = paginator.page(page_num)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)

    context = {'categories': categories, 'subcategories': sub_categories, 'subcategory_products': products,
               'page_obj': page_obj}
    return render(request=request, template_name='products.html', context=context)


def category_products_view(request, category_slug):
    categories = Category.objects.all()
    sub_categories = SubCategory.objects.filter(category_slug__slug=category_slug)
    products = Product.objects.filter(category_slug__slug=category_slug)

    page_num = request.GET.get("page")
    paginator = Paginator(products, 4)
    page_obj = paginator.get_page(page_num)

    try:
        products = paginator.page(page_num)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)

    context = {'categories': categories, 'subcategories': sub_categories, 'category_products': products,
               'page_obj': page_obj}
    return render(request=request, template_name='products.html', context=context)


def all_products_view(request):
    categories = Category.objects.all()
    products = Product.objects.all()

    page_num = request.GET.get("page")
    paginator = Paginator(products, 4)
    page_obj = paginator.get_page(page_num)
    pge = paginator.num_pages
    print(pge)

    try:
        products = paginator.page(page_num)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)

    context = {'categories': categories, 'products': products, 'page_obj': page_obj}
    return render(request=request, template_name='products.html', context=context)


def services_view(request):
    services = Service.objects.all()

    page_num = request.GET.get("page")
    paginator = Paginator(services, 6)
    page_obj = paginator.get_page(page_num)
    pge = paginator.num_pages
    print(pge)

    try:
        services = paginator.page(page_num)
    except PageNotAnInteger:
        services = paginator.page(1)
    except EmptyPage:
        services = paginator.page(paginator.num_pages)

    context = {'services': services, 'page_obj': page_obj}
    return render(request=request, template_name='services.html', context=context)


def news_view(request):
    news = News.objects.all()

    page_num = request.GET.get("page")
    paginator = Paginator(news, 6)
    page_obj = paginator.get_page(page_num)
    pge = paginator.num_pages
    print(pge)

    try:
        news = paginator.page(page_num)
    except PageNotAnInteger:
        news = paginator.page(1)
    except EmptyPage:
        news = paginator.page(paginator.num_pages)

    context = {'news': news, 'page_obj': page_obj}
    return render(request=request, template_name='news.html', context=context)


def company_view(request):
    context = {}
    return render(request=request, template_name='about_company.html', context=context)


def project_view(request):
    context = {}
    return render(request=request, template_name='projects.html', context=context)


def contacts_view(request):
    context = {}
    return render(request=request, template_name='contacts.html', context=context)


def detail_view(request, slug, pk):
    if request.method == "POST":
        form_detail = ApplyForm(request.POST)
        name = request.POST.get('applier_name')
        phone = request.POST.get('applier_phone')
        message = request.POST.get('message')
        if form_detail.is_valid():
            form_detail.applier_name = request.POST.get('applier_name')
            form_detail.applier_phone = request.POST.get('applier_phone')
            form_detail.message = request.POST.get('message')
            form_detail.save()
        print("request.path: ", request.path)
        requests.get(f"http://api.telegram.org/bot{settings.TOKEN}/sendMessage?chat_id={settings.CHANNEL_ID}&text=Поступила заявка :\n\n"
                     f"Имя :  {name}\nНомер телефона :  {phone}\nСообщение :  {message}")
        return HttpResponseRedirect(request.path)
    else:
        # product_get = request.GET.get("product")
        # service_get = request.GET.get("service")
        # new_get = request.GET.get("new")
        product_objects = Product.objects.all()
        service_objects = Service.objects.all()
        product_list = []
        service_list = []
        for item in product_objects:
            product_list.append(item.slug)
        for item in service_objects:
            service_list.append(item.slug)
        product = None
        service = None
        news = None
        if slug in product_list:
            product = Product.objects.get(slug=slug)
        elif slug in service_list:
            print('slug in service')
            service = Service.objects.get(slug=slug)
        else:
            news = News.objects.get(pk=pk)
            year = str(news.date).split(sep="-")[0]
            print(year)

        context = {'product': product, 'service': service, 'news': news}
        return render(request=request, template_name='item-detail.html', context=context)


