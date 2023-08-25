from .models import Cart

def get_cart_data (request):
    if request.user.is_authenticated:
        
    cart = Cart.objects.get(user = request.user)
    return {'cart_data':cart}