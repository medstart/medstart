__author__ = 'komalgupta'
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from login.models import User
class UserForm(UserCreationForm):
    """
    A form that creates a user, with no privileges, from the given email and
    password.
    """

    def __init__(self, *args, **kargs):
        super(UserForm, self).__init__(*args, **kargs)
        del self.fields['username']

    class Meta:
        model = User
        fields = ("email",)

class CustomUserChangeForm(UserChangeForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    password hash display field.
    """

    def __init__(self, *args, **kargs):
        super(CustomUserChangeForm, self).__init__(*args, **kargs)
        del self.fields['username']

    class Meta:
        model = User