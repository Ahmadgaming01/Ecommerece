from django.urls import path
from .views import ProductList , ProductDetail , BrandList,BrandDetail,post_list_debug
from .api import ProductListApi , ProductDetailApi , BrandListApi
app_name = 'products'
urlpatterns = [
    path('debug', post_list_debug),
    path('' , ProductList.as_view(),name='product_list'),
    path('<slug:slug>',ProductDetail.as_view(),name='product_detail'),
    path('Brand/' , BrandList.as_view(),name='brand_list'),
    path('Brand/<slug:slug>',BrandDetail.as_view(),name='brand_detail'),\
    path('api/list' , ProductListApi.as_view()),    
    path('api/list/<int:product_id>' , ProductDetailApi.as_view()),
    path('brands/api/list' , BrandListApi.as_view()),
]