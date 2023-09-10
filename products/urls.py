from django.urls import path
from .views import ProductList , ProductDetail , BrandList,BrandDetail,post_list_debug
from .api import ProductListApi , ProductDetailApi , BrandListApi , BrandDetailApi
app_name = 'products'
urlpatterns = [
    path('debug', post_list_debug),
    path('' , ProductList.as_view(),name='product_list'),
    path('<slug:slug>',ProductDetail.as_view(),name='product_detail'),
    path('Brand/' , BrandList.as_view(),name='brand_list'),
    path('Brand/<slug:slug>',BrandDetail.as_view(),name='brand_detail'),\
    
        #-----------------Api_Path---------------

    path('api/list' , ProductListApi.as_view()),    
    path('api/list/<int:pk>' , ProductDetailApi.as_view()),
    path('brands/api/list' , BrandListApi.as_view()),
    path('brands/api/list/<int:pk>', BrandDetailApi.as_view()),
]