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

# from auth_module.views import Index, index, all_product,product_details,registration
from auth_module.views import index


urlpatterns = [
#     path('create', create_account, name='create'),
    path('index', index, name='index'),
#     path('', index, name='index'),
    # path('all_product', all_product, name='all_product'),
    # path('product_det', product_details, name='product_det'),
    # path('registration', registration, name='registration'),

]
