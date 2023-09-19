from rest_framework import serializers
from .models import Cart , CartDetail ,OrderDetail , Order 

class CartDetailSerializer (serializers.ModelSerializer):
    class Meta:
        model = CartDetail
        fields = '__all__'




class CartSerializer (serializers.ModelSerializer):
    cart_detail = CartDetailSerializer(many=True)

    class Meta:
        model = Cart
        fields = '__all__'


class OrderDetailserializer (serializers.ModelSerializer):

    class Meta:
        model = OrderDetail
        fields = '__all__'

class OrderSerializer (serializers.ModelSerializer):
    order_detail = OrderDetailserializer(many = True)

    
    class Meta:
        model  = Order
        fields = '__all__'
