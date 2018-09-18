from django.contrib import admin
from .product_model import (Category,
                            SubCategory,
                            ProductBasic,
                            ProductGallery,
                            )
from .models import Order
from .slider_Model import Slider


# Register your models here.


class ProductBasicAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'price', 'is_Feature', 'is_newAriavle', 'image']
    search_fields = ['name', 'price', 'sortDec', 'description']
    # filter_vertical = ['phone']
    list_per_page = 15
    list_filter = ['category__mainCat', 'category', 'is_Feature', 'is_newAriavle']

    class Meta:
        Model = ProductBasic


admin.site.register(ProductBasic, ProductBasicAdmin)
admin.site.register(Category)


class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'mainCat']
    list_filter = ['mainCat']

    class Meta:
        Model = SubCategory


admin.site.register(SubCategory, SubCategoryAdmin)
admin.site.register(ProductGallery)


class ProductOrderAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'coustomer_name', 'phone_number']
    search_fields = ['__str__', 'coustomer_name']
    # filter_vertical = ['phone']
    list_per_page = 15
    list_filter = ['product__category']

    class Meta:
        Model = Order


admin.site.register(Order, ProductOrderAdmin)


class SliderAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'image_file', 'buttonText', 'buttonUrl']

    class Meta:
        Model = Slider


admin.site.register(Slider, SliderAdmin)
