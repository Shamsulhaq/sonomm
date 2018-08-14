from django.contrib import admin
from .models import Customer, Area
# Register your models here.

class CustomerAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'phone', 'address', 'area']
    search_fields = ['phone', 'address']
    # filter_vertical = ['phone']
    list_per_page = 15
    list_filter = ['area']

    class Meta:
        Model = Customer


admin.site.register(Customer, CustomerAdmin)
admin.site.register(Area)
