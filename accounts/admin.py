from django.contrib import admin
from .models import User , Adress , Phones ,Profile
# Register your models here.


class PhonesAdmin(admin.TabularInline):
    model = Phones
class AdressAdmin(admin.TabularInline):
    model = Adress

class ProfileAdmin (admin.ModelAdmin):
    #inlines = [PhonesAdmin , AdressAdmin]
    pass



admin.site.register(Profile , ProfileAdmin)
admin.site.register(Phones)
admin.site.register(Adress)
