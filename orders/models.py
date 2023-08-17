from django.db import models
from django.utils import timezone
# Create your models here.



ORDER_STATUS = (
    ("Recieved" ,"Recieved")
    ("Processed" ,"Processed")
    ("Shipped" ,"Shipped")
    ("Delivered" ,"Delivered")
)

class order(models.Model):
    code = models.CharField(max_length=30)
    status = models.CharField(max_length= 20 , choices=ORDER_STATUS)
    order_time = models.DateTimeField(default= timezone.now)
    delivery_time = models.DateTimeField(null=True , blank=True)
class OrderDetail(models.Model):
    pass
