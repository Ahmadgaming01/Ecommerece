from django.shortcuts import render , redirect
from .forms import SignupForm , ActivateUser
from .models import Profile , Phones , Adress
from products.models import Product , Review , Brand
from orders.models import Order
from django.contrib.auth.models import User
from django.contrib.admin.views.decorators import staff_member_required
# Create your views here.
def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data ['email']
            form.save()
    else:
        form=SignupForm()
    return render(request , 'registration/signup.html',{'form':form})

@staff_member_required
def dashboard(request):
    new_products = Product.objects.filter (flag = "New").count()
    sale_products = Product.objects.filter (flag = "sale").count()
    feature_products = Product.objects.filter (flag = "Feature").count()

    products = Product.objects.all().count()
    orders = Order.objects.all().count()
    brands = Brand.objects.all().count()
    reviews = Review.objects.all().count()
    users = User.objects.all().count()
    orders = Order.objects.all().count()
    recieved = Order.objects.filter(status = "Recieved" ).count()
    processed = Order.objects.filter(status = "Processed" ).count()
    shipped = Order.objects.filter(status = "Shipped" ).count()
    delivered = Order.objects.filter(status = "Delivered" ).count()
    

    

    return render (request,'registration/dashboard.html',{
        "new_products":new_products,
        "sale_products":sale_products,
        "feature_products":feature_products,


        'products':products,
        'reviews':reviews,
        'brands':brands,
        'users':users,
        'orders':orders,

        'recieved':recieved,
        'processed':processed,
        'shipped':shipped,
        'delivered':delivered,


    })