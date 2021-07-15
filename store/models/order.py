from django.db import models
from .coustmer import coustmer
from .product import Product
import datetime
class order(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    custmer=models.ForeignKey(coustmer,on_delete=models.CASCADE)
    quantity=models.IntegerField(default=1)
    price=models.IntegerField()
    address=models.CharField(max_length=50,default="" ,blank=True)
    phone_nu=models.CharField(max_length=10,default="" ,blank=True)
    date=models.DateField(default=datetime.datetime.today)
    
def __str__(self,coustmer):
    return coustmer.name

def placeOrder(self):
    self.save()
