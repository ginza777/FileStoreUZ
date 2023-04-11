from django.contrib import admin
from .models import Contact,Search_Book,Search_File

class MyAdmin(admin.ModelAdmin):


    list_display = ['id','text','count_search']




admin.site.register(Contact)
admin.site.register(Search_Book,MyAdmin)
admin.site.register(Search_File,MyAdmin)
# Register your models here.
