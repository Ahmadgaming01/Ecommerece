from rest_framework import serializers
from .models import Cart , CartDetail ,OrderDetail , Order 

class CartDetailSerializer (serializers.ModelSerializer):
    model = CartDetail
    fields = '__all__'




class CartSerializer (serializers.ModelSerializer):
    cart_detail = CartDetailSerializer(many=True)

    model = Cart
    fields = '__all__'