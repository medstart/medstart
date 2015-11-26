__author__ = 'dev'


from django.conf.urls import include, url, patterns
from login.views import *


urlpatterns = patterns('',
                       url(r'^signup_new/$', register_customer, name='signup_customer'),
                       url(r'^signup_merchant/$', register_merchant, name='signup_merchant'),
                       url(r'^login/$', user_login, name='login'),
                       url(r'^logout/$', logout, name='logout'),
                       url(r'^users/reset/password/$', reset_password, name='reset_password'),
                       )
