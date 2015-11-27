from django.contrib import admin

# Register your models here.
from smsandemail.models import EmailLog

admin.site.register(EmailLog)