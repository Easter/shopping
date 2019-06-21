from django.contrib import admin
from .models import Commodity

# Register your models here.
class Commodityadmin(admin.ModelAdmin):
    list_display = ['id','name','price',]

admin.site.register(Commodity,Commodityadmin)
