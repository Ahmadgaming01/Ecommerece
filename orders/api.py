
from rest_framework.response import Response
from rest_framework import generics
from .models import CartDetail , Cart , Order , OrderDetail
from .serializers import CartDetailSerializer , CartSerializer 
from django.contrib.auth.models import User
from products.models import Product


class CartDetailCreateDeleteAPI(generics.GenericAPIView):


    def get (self, request , *args, **kwargs ):
        user = User.objects.get(username=self.kwargs['username'])
        cart , created = Cart.objects.get_or_create (user = user , completed = False)
        data = CartSerializer(cart).data
        return Response ({'Cart:data' , 'Status:200'})
    


    def post (self , request , *args, **kwargs):
        user = User.objects.get(username=self.kwargs['username'])
        product = Product.objects.get (id=request.data['product_id'])
        quantity = int(request.data['quantity'])

        cart = Cart.objects.get(user=user , completed = False)
        cart_data , created = CartDetail.objects.get_or_create (cart= cart , product = product)
        cart_data.price = product.price
        cart_data.quantity = quantity
        cart_total = round(quantity*product.price , 2)
        cart_data.save()
        return Response({'status':200 , 'message':'product was added successfuly ! '})


    def delete (self , request , *args, **kwargs):
        user = User.objects.get(username=self.kwargs['username'])
        cart = Cart.objects.get(user=user , completed = False)
        product = Product.objects.get (id=request.data['product_id'])


        cart_datail = CartDetail.objects.get (cart = cart , product = product)
        cart_datail.delete ()
        return Response ({'status':200 , 'message':'product was deleted successfuly !'})

class OrderListAPI (generics.ListAPIView):
    pass

class OrderDetailAPI (generics.RetrieveAPIView):
    pass
class CreateOrder (generics.GenericAPIView):
    pass 
