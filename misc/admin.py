from django.contrib import admin

# Register your models here.
from django.contrib.admin import ModelAdmin
from misc.models import City,Place,State


class CityAdmin(ModelAdmin):
    admin.site.register(City, ModelAdmin)

class PlaceAdmin(ModelAdmin):
    admin.site.register(Place, ModelAdmin)

class StateAdmin(ModelAdmin):
    admin.site.register(State, ModelAdmin)