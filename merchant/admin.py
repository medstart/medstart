from django.contrib import admin

# Register your models here.
from django.contrib.admin import ModelAdmin
from merchant.models import Merchant,Managers,Office

admin.site.register(Merchant, ModelAdmin)

admin.site.register(Managers, ModelAdmin)

admin.site.register(Office, ModelAdmin)