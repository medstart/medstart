from django.conf.urls import patterns, url
from login.views import *

urlpatterns = patterns('',

   url(r'^merchant/generalinfo/$', merchant_info, name='merchant_info'),

   )