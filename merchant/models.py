from django.db import models

# Create your models here.
class Merchant(models.Model):
    """
        The Merchant Class, Merchant can have several Managers
        (Merchant--> basically i mean to medical shop)
    """

    mer_name = models.CharField(max_length=255, null=True , blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    APR_CHOICE = (
        ('M_A','Approved'),
        ('M_UA','Unapproved')
    )
    status = models.CharField(max_length=4, choices=APR_CHOICE, default="M_UA")

    is_verified = models.BooleanField(default=False)
    MERCHANT_TYPE_CHOICES = (
        ('LIC', 'Licensed'),
        ('GOV', 'Goverment Funded'),
        ('PER', 'Personal Licensed Merchant'),
        )
    phoneno = models.CharField(max_length=11, blank=True, null=True)
    merchant_type = models.CharField(max_length=3, choices=MERCHANT_TYPE_CHOICES, default="LIC")
    description = models.TextField(max_length=500, null=True, blank=True)
    mer_website = models.CharField(max_length=255, null=True, blank=True)
    logo = models.ImageField(max_length=100, upload_to='media/%Y/%m/%d', blank=True, null=True, default=None)

    def __unicode__(self):
        return self.mer_name or u'<No name provided>'


class Managers(models.Model):
    """
        Manager Class, An Merchant can have several Managers.

    """

    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )

    MANAGER_CHOICES = (
        ('P', 'Primary'),
        ('S', 'Secondary'),
    )

    manager_type = models.CharField(max_length=1, choices=MANAGER_CHOICES, default="P")
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    user = models.OneToOneField("login.User", related_name="user_mer")
    first_name = models.CharField(max_length=30, null=False, blank=False)
    last_name = models.CharField(max_length=30, null=False, blank=False)
    merchant = models.ForeignKey("merchant.Merchant", blank=True, null=True)
    # default_pricing = models.ForeignKey('misc.pricing', default=1) TODO LATER
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default="M")
    photo = models.ImageField(max_length=100, upload_to='media/%Y/%m/%d', blank=True, null=True)
    is_verified = models.BooleanField(default=False)
    mobile = models.CharField(max_length=10, blank=True, null=True)

    def __unicode__(self):
        if self.first_name:
            return self.first_name + " " + self.last_name
        else:
            return str(self.user)


###########################################################################################
# Creating the Office Model #

class Office(models.Model):
    """
        To store information about various LOCATION ADDRESS of an merchant.

    """

    mer = models.ForeignKey("merchant.Merchant", blank=True, null=True)
    phoneno = models.CharField(max_length=11, blank=True, null=True)
    address1 = models.CharField(max_length=255, blank=True, null=True)
    address2 = models.CharField(max_length=255, blank=True, null=True)

    place = models.ForeignKey("misc.Place", related_name="office area mer+", blank=True, null=True)
    city = models.ForeignKey("misc.City", related_name="office city mer+", blank=True, null=True)
    state = models.ForeignKey("misc.State", related_name="office state mer+", blank=True, null=True)
    pincode = models.CharField(max_length=6, null=True,blank=True)
    address_verified = models.BooleanField(default=False)

    def __unicode__(self):
        return self.address1 + " " + self.address2 + " " + str(self.place)
