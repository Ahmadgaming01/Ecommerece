from django.shortcuts import render , redirect
from django.views.generic import ListView
from.models import Order , Cart , CartDetail
from products.models import Product
# Create your views here.

class OderList(ListView):
    model = Order

def add_to_cart (request):
    product = Product.objects.get(id=request.POST['product_id'])
    quantity = request.POST['quantity']


    
    cart = Cart.objects.get(user = request.user , completed = False)
    
    cart_detail , created = CartDetail.objects.get_or_create (cart=cart , product=product)
    cart_detail.quantity = quantity
    cart_detail.price = product.price
    cart_detail.total = round (int(quantity) * product.price , 2)
    cart_detail.save()

    return redirect(f'/product/{product.slug}')