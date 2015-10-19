from django.db import models
from django.conf import settings

# Create your models here.
class Customer(models.Model):
    """
    Customer Class , To store general details of customer

    """
    GENDER_CHOICES = (
    ('M', 'Male'),
    ('F', 'Female')
    )

    STATUS_CHOICES = (
        ('R', 'Registered'),
        ('RET', 'Returning'),
      )

    user = models.OneToOneField('login.User', related_name="customer_user", null=True, blank=True)
    created_on = models.DateTimeField(auto_now_add=True, blank=True)
    updated_on = models.DateTimeField(auto_now=True, blank=True)
    source = models.ForeignKey("login.User", related_name="source_of_data", null=True, blank=True)
    first_name = models.CharField(max_length=30, null=False, blank=False, db_index=True)
    last_name = models.CharField(max_length=30, null=False, blank=False, db_index=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, null=True,blank=True, default=None, db_index=True)
    status = models.CharField(max_length=3, choices=STATUS_CHOICES, default='R', blank=True)

    def __unicode__(self):
        if self.first_name and not self.first_name == '':
            return self.first_name + ' ' + self.last_name
        else:
            if self.user:
                return str(self.user.mobile)
            else:
                return "Error"


class Contact(models.Model):
    """
        To store contact details of customer
    """
    customer_id = models.OneToOneField(Customer, primary_key=True, verbose_name="customer id")
    current_address1 = models.CharField(max_length=255, blank=True, null=True)
    current_address2 = models.CharField(max_length=255, blank=True, null=True)
    place = models.ForeignKey("misc.Place", verbose_name="place name", blank=True, null=True)
    current_pincode = models.CharField(max_length=6, null=True,blank=True)
    def __unicode__(self):
        return self.customer_id.first_name + " " + self.customer_id.last_name + "'s contact details"

class Delivery(models.Model):
    """
        To store delivery details of customer
    """
    customer_id = models.OneToOneField(Customer, primary_key=True, verbose_name="customer id")
    del_address1 = models.CharField(max_length=255, blank=True, null=True)
    del_address2 = models.CharField(max_length=255, blank=True, null=True)
    place = models.ForeignKey("misc.Place", verbose_name="place name", blank=True, null=True)
    del_pincode = models.CharField(max_length=6, null=True,blank=True)
    def __unicode__(self):
        return self.customer_id.first_name + " " + self.customer_id.last_name + "'s delivery details"
