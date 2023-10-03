from django.shortcuts import render , redirect
from django.views.generic import ListView
from.models import Order , Cart , CartDetail , Copon
from products.models import Product
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here. 

class OderList( LoginRequiredMixin, ListView):
    model = Order

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(user=self.request.user)
        return queryset
    
def checkout_page(request):
    cart = Cart.objects.get(user = request.user , completed=False)
    cart_detail = CartDetail.objects.filter(cart=cart)
    return render (request , 'orders/checkout.html',{'cart_detail':cart_detail})


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