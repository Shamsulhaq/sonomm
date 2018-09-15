from django.shortcuts import render,get_object_or_404
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

from ecommarce.product_model import ProductBasic,SubCategory,Category


def index(request):
    orproducts = ProductBasic.objects.order_by('-timestamp').filter(category__mainCat__name='Organic')
    products = ProductBasic.objects.order_by('-timestamp')
    category = Category.objects.all()
    categorys =SubCategory.objects.filter(mainCat__name="Organic")
    paginator = Paginator(products, 8)  # Show 8 contacts per page
    page = request.GET.get('page')
    products = paginator.get_page(page)
    paginator = Paginator(orproducts,8)
    page = request.GET.get('page')
    orproducts = paginator.get_page(page)
    context = {
        'orproducts':orproducts,
        'products':products,
        'cats':categorys,
        'cat':category

    }
    return render(request, 'index.html',context)
