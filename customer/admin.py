from django.contrib import admin

# Register your models here.
from django.contrib.admin import ModelAdmin
from customer.models import Customer , Delivery , Contact


class Customer(ModelAdmin):
    admin.site.register(Customer, ModelAdmin)

class Contact(ModelAdmin):
    admin.site.register(Contact, ModelAdmin)

class Delivery(ModelAdmin):
    admin.site.register(Delivery, ModelAdmin)