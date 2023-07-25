from django.shortcuts import render ,redirect
from django.views import generic
from.models import Product , ProductImages ,Brand ,Review
from django.db.models import Q


def post_list_debug (request):
    #data = Product.objects.filter(price=20)
    #data = Product.objects.filter(price__gt=80)
    #data = Product.objects.filter(price_lt=20)
    #data = Product.objects.filter(price__lte=80)
    #data = Product.objects.filter(price__range=(20,25))
    #data = Product.objects.filter(brand__id__gt=30)
    #data = Product.objects.filter(name__contains='snyder')
    #data = Product.objects.filter(name__startswith='logon')
    #data = Product.objects.filter(name__endwith='snyder')
    #data = Product.objects.filter(video__isnull=True)
    #data = Review.objects.filter(create_date_year=2023)
    #data = Review.objects.filter(create_date_month=7)
    #data = Product.objects.filter(price__gt=50, flag='Sale')
    #data = Product.objects.filter(price__gt = 20).filter(flag='Sale')\
    data = Product.objects.filter(
        Q(price__gt=50),
        Q(flag = 'Sale')
        

    )


    return render(request , 'products/debug.html',{'data':data})



class ProductList (generic.ListView):
    model = Product
    paginate_by = 100

class ProductDetail (generic.DetailView):
    model = Product

class BrandList(generic.ListView):
    model = Brand
    paginate_by = 50

class BrandDetail(generic.ListView):
    model = Product
    template_name = 'products/brand_detail.html'

    def get_queryset(self):
        brand = Brand.objects.get(slug = self.kwargs['slug'])
        queryset = Product.objects.filter(brand=brand)
        return queryset
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["brand"] = Brand.objects.get(slug = self.kwargs['slug'])
        return context
    
class DeleteProduct(generic.DeleteView):
    model = Product
    template_name = "delete_product.html"
