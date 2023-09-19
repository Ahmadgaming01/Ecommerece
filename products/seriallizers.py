 from rest_framework import serializers
from .models import Product , Brand
from django.db.models.aggregates import Avg

class ProductSerializer (serializers.ModelSerializer):
    brand = serializers.StringRelatedField()
    review_count = serializers.SerializerMethodField()
    avg_rate = serializers.SerializerMethodField()
    class  Meta:
        model = Product
        fields = '__all__'
    
    def get_review_count (self , object):
        reviews = object.product_review.all().count()
        return reviews
    
    def get_avg_rate (self , object):
        avg = object.product_review.aggregate(avg = Avg ('rating'))
#        if not avg['avg'] :
#            result = 0
#        else:
#            result = round(avg['avg'] , 2)
        
        

        result = 0 if not avg['avg'] else round(avg['avg'] , 2)
        return result
    

class BrandSerializer (serializers.ModelSerializer):
    
    class  Meta:
        model = Brand
        fields = '__all__'

class BrandDetailSerializer (serializers.ModelSerializer):
    products = ProductSerializer (source = 'Product_Brand',many=True)
    class  Meta:
        model = Brand
        fields = '__all__'