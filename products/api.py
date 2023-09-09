from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics
from .seriallizers import ProductSerializer , BrandSerializer
from .models import Product , Brand
'''
@api_view(['GET'])
def product_list_api (request):
    products = Product.objects.all()
    data = ProductSerializer(products , many=True , context={'request':request}).data
    return Response({'data':data})

@api_view(['GET'])
def product_detail_api (request , product_id):
    products = Product.objects.get(id=product_id )
    data = ProductSerializer(products , context={'request':request}).data
    return Response ({'data':data})
'''

class ProductListApi(generics.ListAPIView):
    products = Product.objects.all() 
    serializer_class = ProductSerializer

class ProductDetailApi(generics.RetrieveAPIView):
    products = Product.objects.all() 
    serializer_class = BrandSerializer



class BrandListApi (generics.ListAPIView):
    queryset = Brand.objects.all() 
    serializer_class = BrandSerializer