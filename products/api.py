from rest_framework.decorators import api_view
from rest_framework.response import Response
from .seriallizers import ProductSerializer
from .models import Product


def product_list_api (request):
    products = Product.objects.all()
    data = ProductSerializer(products , many=True).data
    return Response({'data':data})