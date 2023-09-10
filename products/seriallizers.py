from rest_framework import serializers
from .models import Product , Brand


class ProductSerializer (serializers.ModelSerializer):
    brand = serializers.StringRelatedField()
    review_count = serializers.SerializerMethodField()
    class  Meta:
        model = Product
        fields = '__all__'
    
    def get_review_count (self , object):
        reviews = object.product_review.all().count()
        return reviews


class BrandSerializer (serializers.ModelSerializer):
    
    class  Meta:
        model = Brand
        fields = '__all__'

class BrandDetailSerializer (serializers.ModelSerializer):
    products = ProductSerializer (source = 'Product_Brand',many=True)
    class  Meta:
        model = Brand
        fields = '__all__'