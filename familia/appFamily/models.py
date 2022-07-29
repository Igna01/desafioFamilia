from dataclasses import dataclass
from django.db import models

class Family(models.Model):
    name = models.CharField(max_length=10)
    last_name= models.CharField(max_length=15)
    age= models.IntegerField(null=True, blank=True)
    date_of_birth= models.DateField(auto_now_add=True, null=True, blank=True)
    dni = models.IntegerField(null=True, blank=True)
    



