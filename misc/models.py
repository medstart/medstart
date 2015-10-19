from django.db import models

# Create your models here.
class State(models.Model):
    name = models.CharField(max_length=255, unique=True)
    short_name = models.CharField(max_length=10, null=True, blank=True)

    class Meta:
        ordering = ['name']

    def __unicode__(self):
        return self.name

class Place(models.Model):
    name = models.CharField(max_length=255, unique=True)
    short_name = models.CharField(max_length=10, null=True, blank=True)
    place_id = models.CharField(max_length=35, null=True, blank=True, db_index=True)
    location = models.CharField(max_length=255, null=True, blank=True)
    city = models.ForeignKey('City',null=True,blank=True)

    class Meta:
        ordering = ['name']

    def __unicode__(self):
        return self.name

class City(models.Model):
    name = models.CharField(max_length=255, unique=True)
    short_name = models.CharField(max_length=10, null=True, blank=True)
    state = models.ForeignKey('State',null=True,blank=True)

    class Meta:
        ordering = ['name']

    def __unicode__(self):
        return self.name

