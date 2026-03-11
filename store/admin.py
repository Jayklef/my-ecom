from django.contrib import admin
from .models import Product, Disparity

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('product_name',)}
    list_display = ('product_name', 'price', 'stock', 'category', 'modified_date', 'is_available')
    

class DisparityAdmin(admin.ModelAdmin):
    list_display = ('product', 'disparity_category', 'disparity_value', 'is_active')
    list_editable = ('is_active',)
    list_filter = ('product', 'disparity_category', 'disparity_value')
    
   
admin.site.register(Product, ProductAdmin)
admin.site.register(Disparity, DisparityAdmin)
