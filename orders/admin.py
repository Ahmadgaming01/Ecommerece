from django.contrib import admin
from .models import Order , OrderDetail , Cart , CartDetail , Copon

admin.site.register(Order)
admin.site.register(OrderDetail)
admin.site.register(Cart)
admin.site.register(CartDetail)
admin.site.register(Copon)
