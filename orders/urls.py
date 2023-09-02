from django.urls import path
from.views import add_to_cart , OderList
app_name = "orders"
urlpatterns = [
    path('' , OderList.as_view()),
    path('add-to-cart' , add_to_cart),
]
