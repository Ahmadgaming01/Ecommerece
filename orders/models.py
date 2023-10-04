from django.db import models
from django.utils import timezone
from accounts.models import Adress
from products.models import Product
from django.contrib.auth.models import User
from utils.generate_cod import generate_code
# Create your models here.



ORDER_STATUS = (
    ("Recieved" ,"Recieved"),
    ("Processed" ,"Processed"),
    ("Shipped" ,"Shipped"),
    ("Delivered" ,"Delivered")
)

class Order(models.Model):
    user = models.ForeignKey(User,related_name='order_user', on_delete=models.SET_NULL , null=True ,blank=True)
    code = models.CharField(max_length=30 , default=generate_code)
    status = models.CharField(max_length= 20 , choices=ORDER_STATUS)
    order_time = models.DateTimeField(default= timezone.now)
    delivery_time = models.DateTimeField(null=True , blank=True)
    delivery_location = models.ForeignKey(Adress , related_name='delivery_address' , on_delete= models.SET_NULL , null=True , blank=True)
    total = models.FloatField()
    coupon = models.ForeignKey("coupon",  related_name='order_coupon' ,on_delete=models.SET_NULL , null=True , blank=True)
    total_with_coupon = models.FloatField(blank=True,null=True)

    def __str__(self):
        return self.code

class OrderDetail(models.Model):
    order = models.ForeignKey(Order , related_name='order_detail',on_delete= models.CASCADE)
    product = models.ForeignKey(Product , related_name='order_product',on_delete= models.SET_NULL , null=True)
    price = models.FloatField()
    quantity = models.IntegerField()
    def __str__(self):
        return str(self.order)

class Cart(models.Model):
    
    user = models.ForeignKey(User,related_name='cart_user', on_delete=models.SET_NULL , null=True ,blank=True)
    completed = models.BooleanField(default=False)
    coupon = models.ForeignKey("coupon", related_name='cart_coupon' ,on_delete=models.SET_NULL , null=True , blank=True)
    total_with_coupon = models.FloatField(blank=True,null=True)

    def cart_total (self):
        total = 0
        for product in self.cart_detail.all():
            total += product.total
        return round (total , 2)

class CartDetail(models.Model):
    cart = models.ForeignKey(Cart , related_name='cart_detail',on_delete=models.CASCADE)
    product = models.ForeignKey(Product , related_name='cart_product',on_delete= models.CASCADE)
    price = models.FloatField()
    quantity = models.IntegerField(default=1)
    total = models.FloatField (default=0)

class Coupon(models.Model):
    code = models.CharField(max_length=25)
    percentage = models.FloatField()
    start_date = models.DateField(default=timezone.now)
    end_date = models.DateField(default=timezone.now)
    quantity = models.IntegerField()

    def __str__(self):
        return self.code
    