from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.template.loader import get_template
from django.core.mail import EmailMessage
from django.conf import settings

from ecommarce.forms import OrderForm
from ecommarce.product_model import ProductBasic, SubCategory, Category, ProductGallery
from .slider_Model import Slider


def index(request):
    orproducts = ProductBasic.objects.order_by('-timestamp').filter(category__mainCat__name='Organic')
    products = ProductBasic.objects.order_by('-timestamp')
    slider = Slider.objects.all()
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
        'slider': slider

    }
    return render(request, 'index.html', context)


def category(request, name):
    categorys = SubCategory.objects.filter(mainCat__name=name)
    context = {
        'cats': categorys,
        'title': name
    }
    return render(request, 'category/category.html', context)


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
    return render(request, 'product/all_product.html', context)


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


def single_product(request, slug):
    product = get_object_or_404(ProductBasic, slug=slug)
    gallery = ProductGallery.objects.filter(product=product.id)
    name = product.get_category()
    relateds = ProductBasic.objects.filter(category__name=name).exclude(id=product.id)[:5]
    context = {
        'product': product,
        'gallery': gallery,
        'relateds': relateds

    }

    return render(request, 'product_inner.html', context)


def allCategorys(request):
    category = Category.objects.all()
    return render(request, 'category/mcategory.html', {'cats': category})


# def getOrder(request, slug):
#     product = get_object_or_404(ProductBasic, slug=slug)
#     if request.method == 'POST':
#         form = OrderForm(request.POST)
#         if form.is_valid():
#             instance = form.save(commit=False)
#             instance.product = product
#             instance.save()
#             mail_subject = 'Received Order request'
#             message = render_to_string('order_request_mail.html', {
#                 'Customer_name': form.cleaned_data.get('name'),
#                 'Customer_Phone': form.cleaned_data.get('phone'),
#                 'Customer_Email': form.cleaned_data.get('email'),
#                 'Customer_Address': form.cleaned_data.get('address'),
#                 'Product': product.name,
#                 'Available_in_Stock': product.is_stock
#             })
#             to_email = 'bmshamsulhaq65@gmail.com'
#             email = EmailMessage(
#                 mail_subject, message, to=[to_email]
#             )
#             email.send()
#             return HttpResponse('Thanks you ')
#
#         return render(request, 'order.html', {"product": product, 'form': form})
#
#     return HttpResponse("Sorry Try Again")


def getorder(request, slug):
    product = get_object_or_404(ProductBasic, slug=slug)
    form = OrderForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.product = product
        instance.price = product.price
        instance.save()
        mail_subject = 'Received Order request'
        name = form.cleaned_data.get('name')
        phone = form.cleaned_data.get('phone')
        email = form.cleaned_data.get('email')
        addr = form.cleaned_data.get('address')
        area = form.cleaned_data.get('area')
        dele = form.cleaned_data.get('delivery_Method')
        prod = product.name
        abl = product.is_stock

        context = {
            'Customer_name': name,
            'Customer_Phone': phone,
            'Customer_Email': email,
            'Customer_Address': addr,
            'Customer_Area': area,
            'Customer_Delivery': dele,
            'Product': prod,
            'Available_in_Stock': abl,

        }
        message = get_template('mail/order_request_mail.html').render(context)
        to_email = 'muhitrana1978@gmail.com'
        email_from = settings.EMAIL_HOST_USER
        email = EmailMessage(
            mail_subject, message, email_from, to=[to_email, email_from]
        )
        email.content_subtype = 'html'
        email.send()
        # send_mail(mail_subject,message,email_from,[to_email,email_from],fail_silently=False)
        return render(request, 'print_order.html', context)

    return render(request, 'order.html', {"product": product, 'form': form})



