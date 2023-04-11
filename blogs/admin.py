from django.contrib import admin
from .models import Blog




class MyAdmin(admin.ModelAdmin):


    list_display = ['id','title','view','created_data']



admin.site.register(Blog,MyAdmin)
# Register your models here.
