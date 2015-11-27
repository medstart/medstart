from django.contrib import admin

# Register your models here.
from misc.models import City, Place, State


admin.site.register(City)

admin.site.register(Place)

admin.site.register(State)