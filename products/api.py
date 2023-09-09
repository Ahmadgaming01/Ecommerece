from rest_framework.decorators import api_view
from rest_framework.response import Response
from .seriallizers import ProductSerializer
from .models import Product

@api_view(['GET'])
def product_list_api (request):
    products = Product.objects.all()
    data = ProductSerializer(products , many=True).data
    return Response({'data':data})

@api_view(['GET'])
def product_detail_api (request , product_id):
    products = Product.objects.get(id=product_id)
    data = ProductSerializer(products).data
    return Response ({'data':data})