from django.contrib.auth import forms
from django.forms import ModelForm, TextInput, modelformset_factory
from misc.models import *

__author__ = 'dev'


class CityForm(ModelForm):

    class Meta:
        model = City
        widgets = {
            'name': TextInput(attrs={'class': 'form-control name' }),
        }

CityFormSet = modelformset_factory(City, extra=0, form=CityForm,
                                      fields=('name'))

class PlaceForm(ModelForm):

    class Meta:
        model = Place
        widgets = {
            'name': TextInput(attrs={'class': 'form-control name' }),
        }

PlaceFormSet = modelformset_factory(Place, extra=0, form=PlaceForm,
                                      fields=('name'))


class StateForm(ModelForm):

    class Meta:
        model = State
        widgets = {
            'name': TextInput(attrs={'class': 'form-control name' }),
        }

StateFormSet = modelformset_factory(State, extra=0, form=StateForm,
                                      fields=('name'))