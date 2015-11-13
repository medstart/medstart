from django.conf.urls import patterns, url
from merchant.views import *

urlpatterns = patterns('',
                        url(r'^merchant/generalinfo/$', merchant_info, name='merchant_info'),
                        url(r'^merchant/managerinfo/$', manager_info, name='manager_info'),
                        url(r'^merchant/contactinfo/$', mercontact_info, name='mer_contact_info'),
                    )