from django.contrib import admin

# Register your models here.
from .models import File

class MyAdmin(admin.ModelAdmin):


    list_display = ['id','name','download_count','view','coin','created_data']

admin.site.register(File,MyAdmin)