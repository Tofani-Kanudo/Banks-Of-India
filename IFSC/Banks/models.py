from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Banks(models.Model):
    ifsc=models.TextField(max_length=11)
    branch=models.TextField(max_length=200)
    address=models.TextField(max_length=1000)
    city=models.TextField(max_length=100)
    district=models.TextField(max_length=50)
    state=models.TextField(max_length=50)
    bank=models.TextField(max_length=100)
    class Meta:
       db_table=u'Banks'
    def __str__(self):
       return self.ifsc