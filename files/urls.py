from django.urls import path
from .views import *

urlpatterns=[
    path('',files,name='files'),
    path('search_files/',search_files,name='search_files'),
    path('file/<slug:slug>/', file_detail, name='file_detail'),
    path('download_file/', premium_download, name='download_file'),

]

