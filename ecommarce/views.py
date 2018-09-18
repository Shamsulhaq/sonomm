from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

from ecommarce.product_model import ProductBasic, SubCategory, Category,ProductGallery
from .slider_Model import Slider


def index(request):
    orproducts = ProductBasic.objects.order_by('-timestamp').filter(category__mainCat__name='Organic')
    products = ProductBasic.objects.order_by('-timestamp')
    slider   = Slider.objects.all()
    category = Category.objects.all()
    categorys = SubCategory.objects.filter(mainCat__name="Organic")
    paginator = Paginator(products, 8)  # Show 8 contacts per page
    page = request.GET.get('page')
    products = paginator.get_page(page)
    paginator = Paginator(orproducts, 8)
    page = request.GET.get('page')
    orproducts = paginator.get_page(page)

    context = {
        'orproducts': orproducts,
        'products': products,
        'cats': categorys,
        'cat': category,
        'slider':slider

    }
    return render(request, 'index.html', context)


def category(request, name):
    categorys = SubCategory.objects.filter(mainCat__name=name)
    context = {
        'cats': categorys,
        'title': name
    }
    return render(request, 'category.html', context)


def all_product(request, name):
    products = ProductBasic.objects.order_by('-timestamp').filter(category__name=name)
    cat = get_object_or_404(SubCategory, name=name)
    paginator = Paginator(products, 8)  # Show 8 contacts per page
    page = request.GET.get('page')
    products = paginator.get_page(page)
    search = request.GET.get('search')
    if search:
        products = ProductBasic.objects.filter(
            Q(name__icontains=search) |
            Q(description__icontains=search) |
            Q(category__mainCat__name__icontains=search) |
            Q(category__name__icontains=search) |
            Q(sortDec__icontains=search))

    context = {
        "products": products,
        "title": name,
        "ptitle": cat
    }
    return render(request, 'all_product.html', context)


def search(request):
    search = request.GET.get('search')
    if search:
        products = ProductBasic.objects.filter(
            Q(name__icontains=search) |
            Q(description__icontains=search) |
            Q(category__mainCat__name__icontains=search) |
            Q(category__name__icontains=search) |
            Q(sortDec__icontains=search))
        paginator = Paginator(products, 8)  # Show 8 contacts per page
        page = request.GET.get('page')
        products = paginator.get_page(page)

    context = {
        "products": products,
        "title": "Search Result",
    }
    return render(request, 'search_result.html', context)


def single_product(request,slug):
    product = get_object_or_404(ProductBasic,slug=slug)
    gallery= ProductGallery.objects.filter(product = product.id)
    name = product.get_category()
    relateds = ProductBasic.objects.filter(category__name=name).exclude(id =product.id)[:5]
    context = {
        'product':product,
        'gallery':gallery,
        'relateds':relateds

    }

    return render(request, 'product_inner.html', context)
