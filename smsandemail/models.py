from time import timezone
from datetime import datetime
from django.db import models

# Create your models here.


class EmailLog(models.Model):
    receiver = models.TextField()  # textfield because it can store comma separated email addresses
    subject = models.TextField()
    email = models.TextField()
    timestamp = models.DateTimeField(null=True)
    status = models.CharField(max_length=20)

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        if not self.id:
            self.timestamp = datetime.now()
        return super(EmailLog, self).save()

    def __unicode__(self):
        return self.receiver + ": " + self.subject + ", status: " + self.status