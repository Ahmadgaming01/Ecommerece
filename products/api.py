from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics
from .seriallizers import ProductSerializer , BrandSerializer, BrandDetailSerializer
from .models import Product , Brand
import django_filters.rest_framework
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from .filters import ProductFilter

#@api_view(['GET'])
#def product_list_api (request):
   # products = Product.objects.all()
    #data = ProductSerializer(products , many=True , context={'request':request}).data
   # return Response({'data':data})

#@api_view(['GET'])
#def product_detail_api (request , product_id):
    #products = Product.objects.get(id=product_id )
    #data = ProductSerializer(products , context={'request':request}).data
   # return Response ({'data':data})


class ProductListApi(generics.ListAPIView):
    queryset = Product.objects.all() 
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = ProductFilter
#    filter_backends = [filters.SearchFilter]
#    filterset_fields = ['brand', 'flag','name', 'price']
    #search_fields = ['name', 'subtitle']
    #filter_backends = [filters.OrderingFilter]
    #ordering_fields = ['price', 'flag']
    
    
class ProductDetailApi(generics.RetrieveAPIView):
    queryset = Product.objects.all() 
    serializer_class = ProductSerializer



class BrandListApi (generics.ListAPIView):
    queryset = Brand.objects.all() 
    serializer_class = BrandSerializer


class BrandDetailApi (generics.RetrieveAPIView):
    queryset = Brand.objects.all() 
    serializer_class = BrandDetailSerializer