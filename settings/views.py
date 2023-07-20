from django.shortcuts import render
from products.models import Product , Brand , Review
# Create your views here.
def home (requset):
    brands =Brand.objects.all()
    sale_products = Product.objects.filter(flag = 'Sale')[:10]
    feature_products = Product.objects.filter(flag = 'Feature')[:6]
    new_products = Product.objects.filter(flag = 'New')[:6]
    reviwes = Review.objects.all()[:6]

    return render( requset , 'settings/home.html', {
        'brands':brands,
        'feature_products':feature_products,
        'sale_products' : sale_products,
        'new_products' : new_products,
        'reviewes':reviwes,
        'brands_sliced' :brands[:6]

    })