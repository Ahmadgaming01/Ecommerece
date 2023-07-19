from django.shortcuts import render
from products.models import Product , Brand , Review
# Create your views here.
def home (requset):
    brands =Brand.objects.all()
    sale_products = Product.objects.filter(flag = 'Sale')
    feature_products = Product.objects.filter(flag = 'feature')
    new_products = Product.objects.filter(flag = 'new')
    reviwes = Review.objects.all()

    return render( requset , 'settings/home.html', {
        'brands':brands,
        'feature_products':feature_products,
        'sale_products' : sale_products,
        'reviewes':reviwes,
        

    })