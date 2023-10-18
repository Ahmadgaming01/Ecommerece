from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.core.validators import MaxValueValidator, MinValueValidator
from taggit.managers import TaggableManager
from django.utils.translation import gettext_lazy as _
from django.utils.text import slugify
from django.db.models.aggregates import Avg , Count
# Create your models here.

FLAG_TYPES = [
    ('New' , 'New'),
    ('Sale' , 'Sale'),
    ('Feature' , 'Feature'),
]

class Product(models.Model):
        
    name = models.CharField (_('name'),max_length=120)
    description = models.TextField (_('description'),max_length=30000)
    price = models.FloatField (_('price'))
    image = models.ImageField(_('image'),upload_to= "productImage")
    sku = models.IntegerField(_('sku'))
    subtitle = models.TextField(_('subtitle'),max_length=600)
    brand = models.ForeignKey('Brand', verbose_name=_('Brand') ,related_name="Product_Brand" ,on_delete=models.CASCADE)
    flag = models.CharField(_('flag'),max_length=20 ,choices=FLAG_TYPES)
    tags = TaggableManager()
    slug = models.SlugField (blank=True , null= True)
    video = models.URLField(blank=True , null= True)
    
    def __str__(self):
        return self.name
    
    def save(self ,  *args, **kwargs):
        self.slug = slugify(self.name)
        super(Product , self).save(*args,**kwargs)
    def get_avg_rate (self):
        avg = self.product_review.aggregate(avg = Avg ('rating'))


class ProductImages(models.Model):
    product = models.ForeignKey(Product ,verbose_name=_('product') , related_name='images_product', on_delete=models.CASCADE)
    image = models.ImageField(_('images'), upload_to='products_images')
    def __str__(self):
        return str(self.product)   
    
class Brand (models.Model):
    name = models.CharField ( _('name'),max_length=150)
    image = models.ImageField (_('image'),upload_to="brand")
    slug = models.SlugField (blank=True , null= True)
    
    def save(self ,  *args, **kwargs):
        self.slug = slugify(self.name)
        super(Brand , self).save(*args,**kwargs)

    def __str__(self):
        return self.name

class Review (models.Model):
    user = models.ForeignKey(User , verbose_name=_('user') ,related_name='user_review',on_delete=models.SET_NULL , null=True , blank=True)
    product = models.ForeignKey(Product , verbose_name=_('product') , related_name= 'product_review' , on_delete=models.SET_NULL ,null=True , blank= True)
    review = models.TextField (_('review'),max_length=600)
    rate =models.IntegerField(_('rate') ,validators=[MinValueValidator(0), MaxValueValidator(5)])
    date = models.DateTimeField(default= timezone.now)
    def __str__(self):
        return str(self.user)

