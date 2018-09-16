"""Store URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from .views import index, all_product, category,search

urlpatterns = [
    path('', index, name='index'),
    path('index/', index, name='index'),
    path('search/', search, name='search'),
    path('category/<name>', category, name='category'),
    path('products/<name>', all_product, name='products'),
    # /path('index/',Index.as_view(), name='index'),

]