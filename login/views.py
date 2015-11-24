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


def logout(request):
    """
        Log out! the name says it all!
        Corresponding Urls:
        1. /logout
    """
    request.session.flush()
    return HttpResponseRedirect(reverse('index'))

def register_customer(request):
    title = 'signup|medstart'
    user = request.user
    if request.method == 'GET':
        return render(request,"login/signup.html")
    else:
        email = request.POST["email"]
        mobile=request.POST["mobile"]
        password=request.POST["password"]
        u=User()
        try:
            if User.objects.filter(email=email):
                response_data={'Error':'User with this email Already Exists'}
                return HttpResponse(json.dumps(response_data),content_type="application/json")
            elif User.objects.filter(mobile=mobile):
                response_data={'Error':'User with this mobile Already Exists'}
                return HttpResponse(json.dumps(response_data),content_type="application/json")
            else:
                u = User.objects.create(email=email,mobile=mobile,user_type = 'CST',terms=True)
                group = Group.objects.get(name='customer')
                u.set_password(password)
                u.save()
                c = Customer.objects.create(user=u,source=u,first_name="",last_name="")
                c.save()
                group.user_set.add(u)
                u = authenticate(username=email, password=password)
                u.backend = 'django.contrib.auth.backends.ModelBackend'
                login(request, u)
                return HttpResponseRedirect(reverse('index'))
        except Exception , e:
            print e
            return render(request,"login/signup.html")




def register_merchant(request):
    title = 'signup for business | medstart'
    if request.method == 'GET':
        return render(request,"login/signup1.html")
    else:
        merchant = request.POST["merchant"]
        email = request.POST["email"]
        mobile = request.POST["mobile"]
        password = request.POST["password"]
        u = User()
        try:
            if User.objects.filter(email=email):
                response_data = {'Error': 'User with this email Already Exists'}
                return HttpResponse(json.dumps(response_data),content_type="application/json")
            elif User.objects.filter(mobile=mobile):
                response_data = {'Error': 'User with this mobile Already Exists'}
                return HttpResponse(json.dumps(response_data), content_type="application/json")
            else:
                u = User.objects.create(email=email, mobile=mobile, user_type='MER', terms=True)
                group = Group.objects.get(name='merchant')
                u.set_password(password)
                u.save()
                m = Merchant.objects.create(mer_name=merchant, merchant_type='LIC')
                m.save()
                man = Managers.objects.create(user=u, merchant=m)
                man.save()
                group.user_set.add(u)
                u = authenticate(username=email, password=password)
                u.backend = 'django.contrib.auth.backends.ModelBackend'
                login(request, u)
                return HttpResponseRedirect(reverse('index'))
        except Exception, e:
            print e
            return render(request, "login/signup.html")


def userlogin(request):
    title = 'login | medstart'
    if request.method == 'GET':
        return render(request,"login/signin.html")
    else:
        username=request.POST["username"]
        password=request.POST["password"]
        u = User.objects.filter(email=username)
        if u.exists():
            if u[0].check_password(password):
                try:
                    user = authenticate(username=username, password=password)
                    login(request, user)
                    if user.user_type == 'CST':
                        return HttpResponseRedirect(reverse('index'))
                    elif user.user_type == 'MER':
                        return HttpResponseRedirect(reverse('index'))
                except Exception, e:
                    print e
                    response_data={'Error':'Something is wrong, Please try again'}
                    return HttpResponse(json.dumps(response_data),content_type="application/json")
            else:
                response_data={'Error':'Password is wrong, Please enter correct paasword'}
                return HttpResponse(json.dumps(response_data),content_type="application/json")
        else:
            response_data={'Error':'Username does not exist, Please try with registered email id'}
            return HttpResponse(json.dumps(response_data),content_type="application/json")





def reset_password(request):
    title = 'password reset | medstart'
    if request.method == 'GET':
        return render(request,"login/reset.html")

