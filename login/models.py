from django.db import models
from django.utils import timezone
from django.utils.http import urlquote
from django.utils.translation import ugettext_lazy as _
from django.core.mail import send_mail
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager


class UserManager(BaseUserManager):

    def _create_user(self, email, password,
                     is_staff, is_superuser, **extra_fields):
        """
        Creates and saves a User with the given email and password.
        """
        now = timezone.now()
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email,
                          is_staff=is_staff, is_active=True,
                          is_superuser=is_superuser, last_login=now,
                          date_joined=now, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        return self._create_user(email, password, False, False,
                                 **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        return self._create_user(email, password, True, True,
                                 **extra_fields)

class User(AbstractBaseUser, PermissionsMixin):
    """
    A fully featured User model with admin-compliant permissions that uses
    a full-length email field as the username.

    Email and password are required. Other fields are optional.
    """
    username = models.CharField(_('username'),max_length=30,blank=True,null=True)
    email = models.EmailField(_('email address'), max_length=254, unique=True)
    mobile = models.CharField(_('mobile'), max_length=10, null=True, blank=True,unique=True)
    first_name = models.CharField(_('first name'), max_length=30, blank=True)
    last_name = models.CharField(_('last name'), max_length=30, blank=True)
    is_staff = models.BooleanField(_('staff status'), default=False,
        help_text=_('Designates whether the user can log into this admin '
                    'site.'))
    is_active = models.BooleanField(_('active'), default=True,
        help_text=_('Designates whether this user should be treated as '
                    'active. Unselect this instead of deleting accounts.'))
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)
    email_subscribed = models.BooleanField(default=True)
    sms_subscribed = models.BooleanField(default=True)
    activation_key = models.CharField(max_length=255)
    first_time = models.BooleanField(default=False)
    TYPES = (
        ('CST', 'Customer'),
        ('MER', 'Merchant'),
        ('MAN', 'Manpower'),

    )
    terms = models.BooleanField(default=False, blank=True)
    user_type = models.CharField(null=True, blank=True, max_length=3, choices=TYPES)

    objects = UserManager()
    created_by = models.ForeignKey('self', null=True, blank=True, default=None)   # This field is for the User who is creating this User object
    created_on = models.DateTimeField(auto_now_add=True, blank=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
        # Below are the verification fields
    mobile_verified = models.BooleanField(default=False)
    email_verified = models.BooleanField(default=False)

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def get_absolute_url(self):
        return "/users/%s/" % urlquote(self.email)

    def get_full_name(self):
        """
        Returns the first_name plus the last_name, with a space in between.
        """
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        "Returns the short name for the user."
        return self.first_name

    def email_user(self, subject, message, from_email=None):
        """
        Sends an email to this User.
        """
        send_mail(subject, message, from_email, [self.email])