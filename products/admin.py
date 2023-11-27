from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Product , ProductImages , Brand ,Review
from tof.admin import TofAdmin, TranslationTabularInline

# Register your models here.

class ProductImagesAdmin(admin.TabularInline):
    model = ProductImages

class ProductAdmin(SummernoteModelAdmin):
    list_display = ['name','price','brand','flag']
    list_filter = ['price', 'tags' , 'brand' ,'flag']
    search_fields = ['name', 'subtitle' , 'description' ]
    inlines = [ProductImagesAdmin]
    summernote_fields = '__all__'

'''
class TranslationAdmin(TofAdmin):
    list_display = ['name','price','brand','flag']
    list_filter = ['price', 'tags' , 'brand' ,'flag']
    search_fields = ['name', 'subtitle' , 'description' ]
    
    summernote_fields = '__all__'
    only_current_lang = ('description', )
    inlines = (TranslationTabularInline, )
'''

admin.site.register(Product ,ProductAdmin)
admin.site.register(ProductImages)
admin.site.register(Brand)
admin.site.register(Review)


