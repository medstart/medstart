from django.contrib.auth import forms
from django.core.validators import RegexValidator
from django.forms import ModelForm
from customer.models import Customer,Contact,Delivery
from login.models import User
from misc.models import Place

__author__ = 'dev'


attrs_dict = {'class': 'form-control', 'placeholder': 'Enter the email id','type':'email'}
attrs_dict1 = {'class': 'required form-control', 'placeholder': 'Enter the mobile number','type':'tel'}
attrs_dict_req = {'class': 'form-control', 'placeholder': 'Enter the email id','type':'email','required':'required'}




class CustomerInfo(ModelForm):
    email_subscribed = forms.BooleanField(required=False)
    sms_subscribed = forms.BooleanField(required=False)

    class Meta:
        model = Customer
        exclude = ['user', 'source', 'created_on', 'updated_on','status']


        css_class = "form-control"
        select_class = 'form-control m-bot15'
        widgets = {
            'first_name': forms.TextInput(attrs={'class': css_class}),
            'last_name': forms.TextInput(attrs={'class': css_class}),
            'gender': forms.Select(attrs={'class': css_class}),

        }



class ContactForm(forms.ModelForm):
    location = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': "form-control placeautocomplete",'placeholder':"Enter Current Location",'required':'true'}))
    mobile = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': "form-control",'required':'required','type':'tel'}), validators=[
        RegexValidator(regex='^\d{10}$', message='Length has to be 10 digits', code='Invalid number')])

    def __init__(self, *args, **kwargs):
        my_arg = kwargs.pop('my_arg')
        super(ContactForm, self).__init__(*args, **kwargs)
        user = User.objects.get(id=my_arg['uid'])
        try:
            place = Place.objects.get(place_id=self.instance.place.place_id)
            self.fields['location'].initial = str(place.location)
        except:
            pass

    class Meta:
        model = Contact
        css_class = "form-control"
        exclude = ['customer_id', 'current_address1', 'current_address2', 'mobile', 'current_pincode']
        select_class = 'form-control m-bot15'
        widgets = {
        'place':forms.TextInput(attrs={'class': 'form_control hidden placeautocomplete'}),

        }
class DeliveryForm(forms.ModelForm):
    location = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': "form-control placeautocomplete",'placeholder':"Enter Current Location",'required':'true'}))
    mobile = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': "form-control",'required':'required','type':'tel'}), validators=[
        RegexValidator(regex='^\d{10}$', message='Length has to be 10 digits', code='Invalid number')])

    def __init__(self, *args, **kwargs):
        my_arg = kwargs.pop('my_arg')
        super(ContactForm, self).__init__(*args, **kwargs)
        user = User.objects.get(id=my_arg['uid'])
        try:
            place = Place.objects.get(place_id=self.instance.place.place_id)
            self.fields['location'].initial = str(place.location)
        except:
            pass

    class Meta:
        model = Delivery
        css_class = "form-control"
        exclude = ['customer_id', 'del_address1', 'del_address2', 'mobile', 'del_pincode']
        select_class = 'form-control m-bot15'
        widgets = {
        'place':forms.TextInput(attrs={'class': 'form_control hidden placeautocomplete'}),

        }
