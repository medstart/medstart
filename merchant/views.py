from django.shortcuts import render, redirect

# Create your views here.
from merchant.forms import ManagerInfo, OfficeInfo, MerchantInfo
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect


def merchant_info(request):
    title = 'Pharmacy Details | medstart'
    form = MerchantInfo()
    if request.method == 'GET':
        return render(request, "merchant/companyinfo.html", locals())
    else:
        form = MerchantInfo(request.POST, request.FILES)
        if form.is_valid():
            return redirect('manager_info')
        else:
            return render(request, "merchant/companyinfo.html", locals())


def manager_info(request):
    title = 'Manager Details | medstart'
    form = ManagerInfo()
    if request.method == 'GET':
        return render(request, "merchant/managerinfo.html", locals())
    else:
        form = ManagerInfo(request.POST, request.FILES)
        if form.is_valid():
            return redirect('mer_contact_info')
        else:
            return render(request, "merchant/managerinfo.html", locals())


def mercontact_info(request):
    title = 'Office Details | medstart'
    form = OfficeInfo()
    if request.method == 'GET':
        return render(request, "merchant/officeinfo.html", locals())
    else:
        form = OfficeInfo(request.POST, request.FILES)
        if form.is_valid():
            return redirect('index')
        else:
            return render(request, "merchant/officeinfo.html", locals())