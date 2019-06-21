from django.contrib import admin
from .models import User,User_commodity

# Register your models here.
class Useradmin(admin.ModelAdmin):
    list_display = ['id','username','password','email']

class User_commodityAdmin(admin.ModelAdmin):
    list_display = ['id','user','commodity']

admin.site.register(User,Useradmin)
admin.site.register(User_commodity,User_commodityAdmin)
