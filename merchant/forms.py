from django.forms import ModelForm, TextInput, Select, Textarea
from django_select2 import Select2Widget
from merchant.models import *

__author__ = 'dev'


class CompanyInfo(ModelForm):
    class Meta:
        model = Merchant
        exclude = ['created_on', 'updated_on', 'status', 'is_verified','' ]
        css_class = "form-control"
        select_class = 'form-control m-bot15'
        widgets = {
            'mer_name': TextInput(attrs={'class': css_class,'required':'required'}),
            'mer_type': Select(attrs={'class': css_class,'required':'required'}),
            'mer_website': TextInput(attrs={'class': css_class, 'type': 'url'}),
            'description': Textarea(attrs={'class': css_class, 'maxlength': '500','required':'required'}),

        }



class OfficeInfo(ModelForm):
    class Meta:
        model = Office
        exclude = ['mer']
        css_class = "form-control"
        widgets = {
            'phone': TextInput(attrs={'class': css_class,'required':'required'}),
            'add1': TextInput(attrs={'class': css_class,'required':'required'}),
            'add2':TextInput(attrs={'class': css_class,'required':'required'}),
            'place': Select(attrs={'class': css_class,'required':'required'}),
            'city': Select(attrs={'class': css_class,'required':'required'}),
            'state': Select(attrs={'class': css_class,'required':'required'}),
            'pincode' : TextInput(attrs={'class': css_class,'required':'required'}),
        }
