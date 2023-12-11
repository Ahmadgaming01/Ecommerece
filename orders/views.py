from django.shortcuts import render , redirect
from django.views.generic import ListView
from.models import Order , Cart , CartDetail , Coupon , OrderDetail
from products.models import Product
from django.contrib.auth.mixins import LoginRequiredMixin
from settings.models import DeliveryFee
import datetime
from django.http import JsonResponse
from django.template.loader import render_to_string 
from django.conf import settings
import stripe
from utils.generate_cod import generate_code

#for paymnet (user browser session)
from django.contrib.sessions.models import Session
from django.contrib.sessions.backends.db import SessionStore

# Create your views here. 

class OderList( LoginRequiredMixin, ListView):
    model = Order

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(user=self.request.user)
        return queryset
    
def checkout_page(request):
    cart = Cart.objects.get(user = request.user , completed=False)
    cart_detail = CartDetail.objects.filter(cart=cart)
    delivery_fee = DeliveryFee.objects.last ()
    pub_key = settings.STRIPE_API_KEY_PUBLISHBLE

    if request.method=="POST":
        code = request.POST['coupon']
        coupon = Coupon.objects.get(code=code)
        if coupon and coupon.quantity>0:
            today_date = datetime.datetime.today().date()
            if today_date >= coupon.start_date and today_date<= coupon.end_date:
                code_value = cart.cart_total()/100*coupon.percentage
                sub_total = cart.cart_total()-code_value
                total = sub_total + delivery_fee.fee
                cart.coupon = coupon
                cart.total_with_coupon = sub_total
                cart.save()

                html = render_to_string('include/check_out.html', {'cart_detail':cart_detail,
                                                     'delivery_fee':delivery_fee,
                                                     'sub_total':round(sub_total,2),
                                                     'total':round(total,2),
                                                     'discount':round(code_value , 2),
                                                     request:request, 
                                                     'pub_key':pub_key                                                   } )
                return JsonResponse ({'result':html})                

    sub_total = cart.cart_total()
    discount = 0
    total = sub_total + delivery_fee.fee

    return render (request , 'orders/checkout.html',{'cart_detail':cart_detail,
                                                     'delivery_fee':delivery_fee,
                                                     'sub_total':round(sub_total,2),
                                                     'total':round(total,2),
                                                     'discount':discount,
                                                     "pub_key":pub_key
                                                     })


def add_to_cart (request):

    #get data frontend
    product = Product.objects.get(id=request.POST['product_id'])
    quantity = request.POST['quantity']


    #get cart
    cart = Cart.objects.get(user = request.user , completed = False)
    
    # cart detail

    cart_detail , created = CartDetail.objects.get_or_create (cart=cart , product=product)
    cart_detail.quantity = quantity
    cart_detail.price = product.price
    cart_detail.total = round (int(quantity) * product.price , 2)
    cart_detail.save()


    cart = Cart.objects.get(user=request.user , completed=False)
    detail = CartDetail.objects.filter(cart=cart)

    total = f"{cart.cart_total()}$"

    html = render_to_string('include/base_sidebar.html' , {'cart_data':cart , 'cart_detail_data':detail , request:request})
    return JsonResponse({'result':html , 'total':total})
#return redirect(f'/product/{product.slug}')


















# create product on stripe #with ajax

def process_payment(request):
    cart = Cart.objects.get(user = request.user , completed=False)
    cart_detail = CartDetail.objects.filter(cart=cart)
    delivery_fee = DeliveryFee.objects.last ().fee
    if cart.total_with_coupon:
        total = cart.total_with_coupon + delivery_fee
    else:
        cart.cart_total + delivery_fee


    code = generate_code()
    # Save the generated code to the session
    request.session['generated_code'] = code
    request.session.save()

    stripe.api_key = settings.STRIPE_API_KEY_SECRET

    checkout_session = stripe.checkout.Session.create(
        line_items=[
            {
                'price_data':{
                    'currency':'usd',
                    'product_data' :{
                        'name':code
                    },
                    'unit_amount': int (total*100 )
                    
                },
                'quantity':1
                

            },
        ],
        mode='payment',
        success_url='http://127.0.0.1:8000/orders/checkout/payment/success',
        cancel_url='http://127.0.0.1:8000/orders/checkout/payment/failed',
    )
    return JsonResponse({'session':checkout_session})

def payment_success(request):
    cart = Cart.objects.get(user = request.user , completed = False)
    cart_detail = CartDetail.objects.filter(cart=cart)

    generated_code = request.session.get('generated_code')

        #---------create order----------#

    new_order = Order.objects.create (user = request.user , code = generated_code )
    for object in cart_detail:
        OrderDetail.objects.create(
            order=new_order,
            product = object.product,
            price = object.price,
            quantity = object.quantity,
            total = object.total,)
        

        cart.completed=True
        cart.save ()
        
    
    return render(request , 'orders/success.html' , {
        "code":generate_code 
    })

def payment_failed(request):
    return render(request , 'orders/failed.html' , {})