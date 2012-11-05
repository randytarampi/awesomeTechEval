from django.db import models

# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=80)
    birthday = models.DateField()
    gift_bought = models.BooleanField()

    def __unicode__(self):
        return u"%s" % self.name
