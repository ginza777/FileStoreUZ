from django.contrib import admin
from  .models import  Books

class MyAdmin(admin.ModelAdmin):


    list_display = ['name','id','download_count','view','coin','created_data','star']



admin.site.register(Books,MyAdmin)
# Register your models here.
