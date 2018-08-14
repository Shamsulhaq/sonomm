from django.contrib import admin
from .product_model import Category, ProductBasic, ProductGallery


# Register your models here.


class ProductBasicAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'price', 'is_Feature', 'is_newAriavle', 'image']
    search_fields = ['__str__', 'price', ]
    # filter_vertical = ['phone']
    list_per_page = 15
    list_filter = ['category', 'is_Feature', 'is_newAriavle']

    class Meta:
        Model = ProductBasic


admin.site.register(ProductBasic, ProductBasicAdmin)
admin.site.register(Category)
admin.site.register(ProductGallery)
