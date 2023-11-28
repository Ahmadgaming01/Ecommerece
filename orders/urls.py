from django.urls import path
from.views import add_to_cart , OderList , checkout_page , process_payment , payment_success , payment_failed
from .api import CartDetailCreateDeleteAPI , CreateOrderAPI , OrderListAPI , OrderDetailAPI
app_name = "orders"
urlpatterns = [
    path('' , OderList.as_view()),
    path('add-to-cart' , add_to_cart , name='add_to_cart'),
    path ('checkout',checkout_page),
    path ('checkout/payment',process_payment),
    path ('checkout/payment/success',payment_success),
    path ('checkout/payment/failed',payment_failed),
    #-----api--------#

    path ('api/<str:username>/cart' , CartDetailCreateDeleteAPI.as_view()),
    path ('api/<str:username>/cart/create-order' , CreateOrderAPI.as_view()),

    path ('api/<str:username>/orders' , OrderListAPI.as_view()),
    path ('api/<str:username>/orders/<int:pk>' , OrderDetailAPI.as_view()),

    ]
    
