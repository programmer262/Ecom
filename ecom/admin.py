from django.contrib import admin
from .models import *


admin.site.site_header = "Store model"
admin.site.site_title = "Store model"

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['name','email']
    search_fields = ['email']

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['first_name','last_name','email_account']
    search_fields = ['email_account']
@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ['product','order']
    search_fields = ['order']
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id','transaction_id','complete']
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    search_fields = ['name','price']
@admin.register(ShippingAddress)
class ShippingAddressAdmin(admin.ModelAdmin):
    list_display = ['customer','city','country','phone','livraison','time']
    search_fields = ['country','phone']
@admin.register(Information)
class InformationAdmin(admin.ModelAdmin):
    list_display = ['customer','phone','country','city','zipcode']
    search_fields = ['customer','phone']
@admin.register(Company_slider)
class Company_sliderAdmin(admin.ModelAdmin):
      list_display = ['text','description']
      search_fields = ['text']
