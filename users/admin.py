from django.contrib import admin
from .models import User_coin



class MyAdmin(admin.ModelAdmin):


    list_display = ['id','user','coins','email','created_data']

admin.site.register(User_coin,MyAdmin)
# Register your models here.
