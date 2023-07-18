from django.urls import path
from .views import ProductList , ProductDetail , BrandList,BrandDetail

app_name = 'products'
urlpatterns = [
    path('' , ProductList.as_view(),name='product_list'),
    path('<slug:slug>',ProductDetail.as_view(),name='product_detail'),
    path('Brand/' , BrandList.as_view(),name='brand_list'),
    path('Brand/<slug:slug>',BrandDetail.as_view(),name='brand_detail'),
    
]