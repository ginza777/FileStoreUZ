from django.urls import path
from .views import *
from django.urls import re_path as url
from django.views.static import serve

urlpatterns=[
    path('',books,name='books'),
    path('book/<slug:slug>/',book_detail,name='book_detail'),
    path('search_books/',search_books,name='search_books'),
    # path('download_book/',free_download,name='download_book'),
    path('download_book/',premium_download,name='download_book'),




]