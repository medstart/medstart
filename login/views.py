from django.contrib.auth import authenticate, login
from django.contrib.auth.models import Group
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django_extensions.db.fields import json
from customer.models import Customer
from login.models import User
from merchant.models import Merchant, Managers
from misc.helper import send_wemed_mail


def logout(request):
    """
        Log out! the name says it all!
        Corresponding Urls:
        1. /logout
    """
    request.session.flush()
    return HttpResponseRedirect(reverse('index'))


def register_customer(request):
    title = 'signup | wemed'
    user = request.user
    if request.method == 'GET':
        return render(request, "login/signup.html")
    else:
        email = request.POST["email"]
        mobile = request.POST["mobile"]
        password = request.POST["password"]
        try:
            if User.objects.filter(email=email):
                response_data = {'Error': 'User with this email Already Exists'}
                return HttpResponse(json.dumps(response_data),
                                    content_type="application/json")
            elif User.objects.filter(mobile=mobile):
                response_data = {
                    'Error': 'User with this mobile Already Exists'}
                return HttpResponse(json.dumps(response_data),
                                    content_type="application/json")
            else:
                user = User.objects.create(email=email, mobile=mobile,
                                           user_type='CST', terms=True)
                group = Group.objects.get(name='customer')
                user.set_password(password)
                user.save()
                customer = Customer.objects.create(user=user, source=user,
                                                   first_name="", last_name="")
                customer.save()
                group.user_set.add(user)
                user = authenticate(username=email, password=password)
                user.backend = 'django.contrib.auth.backends.ModelBackend'
                login(request, user)
                return HttpResponseRedirect(reverse('index'))
        except Exception, e:
            print e
            return render(request, "login/signup.html")


def register_merchant(request):
    title = 'signup for business | wemed'
    if request.method == 'GET':
        return render(request, "login/signup1.html")
    else:
        merchant = request.POST["merchant"]
        email = request.POST["email"]
        mobile = request.POST["mobile"]
        password = request.POST["password"]
        try:
            if User.objects.filter(email=email):
                response_data = {'Error': 'User with this email Already Exists'}
                return HttpResponse(json.dumps(response_data),
                                    content_type="application/json")
            elif User.objects.filter(mobile=mobile):
                response_data = {'Error': 'User with this mobile Already Exists'
                                 }
                return HttpResponse(json.dumps(response_data),
                                    content_type="application/json")
            else:
                user = User.objects.create(email=email, mobile=mobile,
                                           user_type='MER', terms=True)
                group = Group.objects.get(name='merchant')
                user.set_password(password)
                user.save()
                merchant = Merchant.objects.create(mer_name=merchant,
                                                   merchant_type='LIC')
                merchant.save()
                man = Managers.objects.create(user=user, merchant=merchant)
                man.save()
                # email to merchant
                client_name = merchant.mer_name
                email_context = {
                    'message': 'Hello This is Testing',
                    'business_name': client_name
                }
                recipient = 'komalkgupta@live.com'
                send_wemed_mail('email_templates/merchant/'
                                'welcome_merchant.html', email_context,
                                'email_templates/merchant/'
                                'welcome_merchant_subject.txt', recipient,
                                cc_list=[
                                    'coolkomal09@gmail.com'])
                group.user_set.add(user)
                user = authenticate(username=email, password=password)
                user.backend = 'django.contrib.auth.backends.ModelBackend'
                login(request, user)
                return HttpResponseRedirect(reverse('merchant_info'))
        except Exception, e:
            print e
            return render(request, "login/signup.html")


def user_login(request):
    title = 'login | wemed'
    if request.method == 'GET':
        return render(request, "login/signin.html")
    else:
        username = request.POST["username"]
        password = request.POST["password"]
        user = User.objects.filter(email=username)
        if user.exists():
            if user[0].check_password(password):
                try:
                    user = authenticate(username=username, password=password)
                    login(request, user)
                    if user.user_type == 'CST':
                        return HttpResponseRedirect(reverse('index'))
                    elif user.user_type == 'MER':
                        return HttpResponseRedirect(reverse('index'))
                except Exception, e:
                    print e
                    response_data = {'Error': 'Something is wrong, '
                                              'Please try again'}
                    return HttpResponse(json.dumps(response_data),
                                        content_type="application/json")
            else:
                response_data = {'Error': 'Password is wrong, '
                                          'Please enter correct password'}
                return HttpResponse(json.dumps(response_data),
                                    content_type="application/json")
        else:
            response_data = {'Error': 'Username does not exist,'
                                      ' Please try with registered email id'}
            return HttpResponse(json.dumps(response_data),
                                content_type="application/json")


def reset_password(request):
    title = 'password reset | wemed'
    if request.method == 'GET':
        return render(request, "login/reset.html")

