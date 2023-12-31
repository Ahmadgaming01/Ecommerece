from django.shortcuts import render ,redirect
from django.views import generic
from.models import Product , ProductImages ,Brand ,Review
from .forms import ReviewForm
from django.db.models import Q , F , Value , Func
from django.db.models.aggregates import Count , Avg ,Sum, Min,Max
from django.http import JsonResponse
from django.template.loader import render_to_string 
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator
from .tasks import send_m_email

#@cache_page(60 * 1)


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
    #data = Product.objects.filter(
    #    Q(price__gt=50)|
    #    ~ Q(flag = 'Sale'))
    # data = Product.objects.filter(sku=F('price'))
    #data = Product.objects.filter(sku=F('brand__id'))
    #data = Product.objects.all().order_by('-name')  #reverse
    #data = Product.objects.all().order_by('name')
    #data = Product.objects.order_by('name')
    #data = Product.objects.filter(brand_id=1).order_by('name')
    #data = Product.objects.order_by('flag','name')
    #data = Product.objects.all().order_by('name').last()
    #data = Product.objects.all()[:5]
    #data = Product.objects.all()[5:10]
    #data = Product.objects.values('name','flag','price','brand__name')  #values dictionery
    #data = Product.objects.values_list('name','flag','price','brand__name') #values tuple
    #data = Product.objects.values('name','flag','price','brand__name').distinct()    #no repli.
    #data = Product.objects.defer('tags')   #alle colons auser dem tags
    #data = Product.objects.select_related('brand').all()  #use onToOne, OneToMany
    #data = Product.objects.prefetch_related('brand').all() #use OnToMany
    #data = Product.objects.aaggregate(Count('id'))
    #data = Product.objects.aaggregate(Sum('id'))
    #data = Product.objects.aaggregate(Max('id'))
    #data = Product.objects.aaggregate(mymin = Min('price') , mycount = Count('id'))
    #data = Product.objects.annotate(is_new = Value(True))
    #data = Product.objects.annotate(is_tax = F('price')*1.2)
    #data = Brand.objects.annotate(posts = Count('Product_Brand'))
    data = Product.objects.all()

    #send email 1m user
    
    send_m_email.delay()

    return render(request , 'products/debug.html',{'data':data})

@method_decorator(cache_page(60 * 5), name='dispatch')
class ProductList (generic.ListView):
    model = Product
    paginate_by = 100

class ProductDetail (generic.DetailView):
    model = Product

    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["reviews"] = Review.objects.filter(product=self.get_object())
        return context
    

def add_review(request,slug):
    product = Product.objects.get(slug=slug)
    form = ReviewForm(request.POST)
    if form.is_valid():
        myform = form.save(commit=False)
        myform.product = product
        myform.user = request.user
        myform.save()

        reviews = Review.objects.filter(product=product)
        html = render_to_string('include/all_reviews.html' , {'reviews':reviews , request:request} )
        return JsonResponse ({'result':html})
        #return redirect(f'/products/{product.slug}')


class BrandList(generic.ListView):
    model = Brand
    paginate_by = 50
    
    def get_queryset(self):
        object_list  = Brand.objects.annotate(posts_count = Count('Product_Brand'))
        return object_list
    

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
