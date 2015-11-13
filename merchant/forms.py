from django.core.validators import RegexValidator
from django.forms import ModelForm, TextInput, Select, Textarea, CharField, FileInput
from merchant.models import *

__author__ = 'dev'


class MerchantInfo(ModelForm):
    class Meta:
        model = Merchant
        exclude = ['created_on', 'updated_on', 'status', 'is_verified']
        css_class = "form-control"
        select_class = 'form-control m-bot15'
        widgets = {
            'mer_name': TextInput(attrs={'class': css_class, 'required': 'required'}),
            'merchant_type': Select(attrs={'class': css_class, 'required': 'required'}),
            'mer_website': TextInput(attrs={'class': css_class, 'type': 'url'}),
            'description': Textarea(attrs={'class': css_class, 'maxlength': '500', 'required': 'required'}),
            'phoneno': TextInput(attrs={'class': css_class, 'maxlength': '11', 'type': 'tel', 'required': 'required'}),
             'logo': FileInput(attrs={'class': css_class,'accept':'image/jpg,image/png,image/jpeg,image/gif'}),
        }




class OfficeInfo(ModelForm):
    class Meta:
        model = Office
        exclude = ['mer']
        css_class = "form-control"
        widgets = {
            'phone': TextInput(attrs={'class': css_class, 'required': 'required'}),
            'address1': TextInput(attrs={'class': css_class, 'required': 'required'}),
            'address2': TextInput(attrs={'class': css_class, 'required': 'required'}),
            'pincode': TextInput(attrs={'class': css_class, 'required': 'required', 'maxlength': '6'}),
        }


class ManagerInfo(ModelForm):
    mobile = CharField(required=False, widget=TextInput(attrs={'class': "form-control", 'placeholder': "Enter your mobile number", 'required':'required','type':'tel'}), validators=[
                RegexValidator(regex='^\d{10}$', message='Length has to be 10 digits', code='Invalid number')])

    class Meta:
        model = Managers
        exclude = ['created_on', 'updated_on', 'user', 'merchant', 'is_verified', 'manager_type']
        css_class = "form-control"
        widgets = {
            'first_name': TextInput(attrs={'class': css_class, 'required': 'required'}),
            'last_name': TextInput(attrs={'class': css_class, 'required': 'required'}),
            'gender': Select(attrs={'class': css_class, 'required': 'required'}),
            'photo': FileInput(attrs={'class': css_class, 'accept': 'image/jpg,image/png,image/jpeg,image/gif'}),
        }