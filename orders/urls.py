from django.urls import path
from.views import add_to_cart , OderList , checkout_page
from .api import CartDetailCreateDeleteAPI , CreateOrderAPI , OrderListAPI , OrderDetailAPI
app_name = "orders"
urlpatterns = [
    path('' , OderList.as_view()),
    path('add-to-cart' , add_to_cart),
    path ('checkout',checkout_page),

    #-----api--------#

    path ('api/<str:username>/cart' , CartDetailCreateDeleteAPI.as_view()),
    path ('api/<str:username>/cart/create-order' , CreateOrderAPI.as_view()),

    path ('api/<str:username>/orders' , OrderListAPI.as_view()),
    path ('api/<str:username>/orders/<int:pk>' , OrderDetailAPI.as_view()),

    ]
    
