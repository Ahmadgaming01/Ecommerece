from django.db import models
from django.utils import timezone
from accounts.models import Adress
from products.models import Product
from django.contrib.auth.models import User
# Create your models here.



ORDER_STATUS = (
    ("Recieved" ,"Recieved")
    ("Processed" ,"Processed")
    ("Shipped" ,"Shipped")
    ("Delivered" ,"Delivered")
)

class Order(models.Model):
    user = models.ForeignKey(User,related_name='order_user', on_delete=models.SET_NULL , null=True ,blank=True)
    code = models.CharField(max_length=30)
    status = models.CharField(max_length= 20 , choices=ORDER_STATUS)
    order_time = models.DateTimeField(default= timezone.now)
    delivery_time = models.DateTimeField(null=True , blank=True)
    delivery_location = models.ForeignKey(Adress , related_name='delivery_address' , on_delete= models.SET_NULL , null=True , blank=True)
    total = models.FloatField()
    def __str__(self):
        return self.code

class OrderDetail(models.Model):
    order = models.ForeignKey(Order , related_name='order_detail',on_delete= models.CASCADE)
    product = models.ForeignKey(Product , related_name='order_product',on_delete= models.SET_NULL , null=True)
    price = models.FloatField()
    quantity = models.IntegerField()
    def __str__(self):
        return self.str(self.order)
    
class Cart(models.Model):
    
    user = models.ForeignKey(User,related_name='cart_user', on_delete=models.SET_NULL , null=True ,blank=True)
    completed = models.BooleanField(default=False)

class CartDetail(models.Model):
    cart = models.ForeignKey(Cart , related_name='cart_detail',on_delete=models.CASCADE)
    oder = models.ForeignKey(Order , related_name='order_detail',on_delete= models.CASCADE)
    price = models.FloatField()
    quantity = models.IntegerField()
    total = models.FloatField()