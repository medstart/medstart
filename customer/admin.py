from django.contrib import admin
from customer.models import Customer, Delivery, Contact

admin.site.register(Customer)

admin.site.register(Contact)

admin.site.register(Delivery)
