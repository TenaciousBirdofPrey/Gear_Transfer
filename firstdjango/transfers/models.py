from django.db import models
from decimal import Decimal

# Create your models here.
class Hotels(models.Model):
    hotel_name = models.CharField(max_length = 25)
    #hotel_num =models.IntegerField()
    #hotel_address = models.CharField(max_length = 45)
    latt = models.DecimalField(max_digits=20,decimal_places=10)
    long = models.DecimalField(max_digits=20, decimal_places=10)

class Transfers(models.Model):
	from_loc = models.CharField(max_length = 10)
	to_loc = models.CharField(max_length = 10)
	item = models.CharField(max_length= 20)

