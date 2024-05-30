from django.db import models

# Create your models here.
class ContactpageData(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    mobile = models.BigIntegerField()
    skill = models.CharField(max_length=100)
    location = models.CharField(max_length=200)