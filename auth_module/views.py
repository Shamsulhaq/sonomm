from django.db.models import Q
from django.shortcuts import render, redirect, render



# Create Account.
def index(request):
    return render(request, 'index.html')

#
# def all_product(request):
#     return render(request, 'all_product.html')
#
#
# def product_details(request):
#     return render(request, 'product_inner.html')
#
#
# def registration(request):
#     return render(request, 'registration.html')
#

