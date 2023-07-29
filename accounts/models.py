from django.db import models
from django.contrib.auth.models import User




class Profile (models.Model):
    user = models.ForeignKey(User , related_name= 'User_Profile' , on_delete= models.CASCADE)
    image = models.ImageField(upload_to='accounts')


PHONE_CHOICES = [
    ('Primary','Primary')
    ('Secondary','Secondary')
    
]
 
class Phones (models.Model):
    user = models.ForeignKey(User , related_name= 'User_Phones' , on_delete= models.CASCADE)
    type = models.CharField(max_length=10 , choices=PHONE_CHOICES)
    phone = models.CharField(max_length=25)


ADRESS_CHOICES = [
    ('Home','Home')
    ('Office','Office')
    ('Bussines','Bussines')
    ('Academy','Academy')
    ('Other','Other')
]
    

class Adress(models.Model):
    user = models.ForeignKey(User , related_name= 'User_Adress' , on_delete= models.SET_NULL)
    type = models.TextField(max_length=150 , choices= ADRESS_CHOICES)

