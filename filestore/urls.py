"""filestore URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import re_path as url
from django.urls import path,include
from django.views.static import serve
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    #####apps
    path('accounts2/',include('users.urls'),name='accounts'),
    path('adminpanel/',include('adminpanel.urls'),name='adminpanel'),
    path('blogs/',include('blogs.urls'),name='blogs'),
    path('',include('books.urls')),
    path('files/',include('files.urls'),name='files'),
    path('parsing/',include('parsing.urls'),name='parsing'),




    ########

    url(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    url(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
]
