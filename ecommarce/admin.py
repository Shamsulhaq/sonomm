from django.contrib import admin
from .product_model import (Category,
                            SubCategory,
                            ProductBasic,
                            ProductGallery,

                            )
from .models import Order
from .slider_Model import Slider ,LimitedOffer,GetEmail
from .inspiring_remark_model import InspiringRemark


# Register your models here.


class ProductBasicAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'regular_price', 'price', 'get_discunts', 'is_Feature', 'is_newAriavle', 'is_stock',
                    'is_Friday', 'is_out_stock', 'is_slide']
    search_fields = ['name', 'price', 'sortDec', 'description']
    # filter_vertical = ['category__mainCat__name']
    list_per_page = 15
    list_filter = ['category__mainCat', 'category', 'is_Feature', 'is_newAriavle']

    class Meta:
        Model = ProductBasic


admin.site.register(ProductBasic, ProductBasicAdmin)
admin.site.register(Category)
admin.site.register(GetEmail)


class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'mainCat']
    list_filter = ['mainCat']

    class Meta:
        Model = SubCategory


admin.site.register(SubCategory, SubCategoryAdmin)
admin.site.register(ProductGallery)


class ProductOrderAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'name', 'phone', 'price', 'total_price', 'timestamp', 'delivery_Method', 'is_confirm',
                    'is_paid', 'is_done']
    search_fields = ['name', 'phone']
    # filter_vertical = ['phone']
    list_per_page = 15
    list_filter = ['delivery_Method', 'is_done', 'is_confirm', 'is_paid', 'product__category']

    class Meta:
        Model = Order


admin.site.register(Order, ProductOrderAdmin)


class SliderAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'active', 'timestamp', 'image_file', 'buttonText', 'buttonUrl']

    class Meta:
        Model = Slider


admin.site.register(Slider, SliderAdmin)


class RemarkAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'remarks', 'is_in_font', 'active', 'des', 'fb', 'twi', 'sky', 'timestamp']

    class Meta:
        Model = InspiringRemark


admin.site.register(InspiringRemark, RemarkAdmin)


class OfferAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'last_date', 'active','timestamp']

    class Meta:
        Model = LimitedOffer


admin.site.register(LimitedOffer, OfferAdmin)
