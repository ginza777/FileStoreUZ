from django.http import HttpResponse, Http404, StreamingHttpResponse, FileResponse
from django.shortcuts import render,redirect
from .models import *
# Create your views here.
from blogs.models import Blog
from adminpanel.models import  Contact,Search_File
from django.conf import settings
import os
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib import messages

from users.models import User_coin
def files(requests):
    files=File.objects.all()
    data=[]
    for i in files:
        i = {
            'name': i.name,
            'img': i.img.url,
            'count': i.download_count,
            'slug': i.slug,
            'view':i.view,
            'title':i.title,
            'coin':i.coin,

        }
        data.append(i)
        blogs = Blog.objects.all()
        contact = Contact.objects.last()
    data_trend = sorted(data, key=lambda d: d['count'])[::7]


    ####################blog
    blogs=Blog.objects.all()

        ######################Contact

    contact=Contact.objects.last()



    return render(requests,'book/files.html',{'files':data,'data_trend':data_trend,'blogs':blogs,'contact':contact})


def file_detail(request,slug):
    fayl=File.objects.get(slug=slug)
    fayl.view+=1
    fayl.save()

    data={
        'name': fayl.name,
        'img': fayl.img.url,
        'count': fayl.download_count,
        'title':fayl.title,
        'file':fayl.file.url,
        'coin':fayl.coin,
        'slug': slug,
        'view':fayl.view,



    }


    return render(request,'book/file_detail.html',{'file':data})


def search_files(request):
    search = request.POST.get('search')
    if search:
        if search:
            if Search_File.objects.filter(text=search):

                a = Search_File.objects.get(text=search)
                a.count_search += 1
                a.save()


            else:
                Search_File.objects.create(text=search).save()


        search=request.POST.get('search')
        print(search)
        search_file =File.objects.filter(tag__contains=search)
        if search_file:


            data_file = []
            for file in search_file:

                context = {
                    'name': file.name,
                    'img': file.img.url,
                    'coin': file.coin,
                    'slug': file.slug,
                    'count': file.download_count,
                    'title': file.title,
                    'file': file.file.url,
                    'view': file.view

                }
                data_file.append(context)

            return render(request, 'book/file_search.html', {'search_files': data_file, 'search':search})
        else:
            messages.error(request, "ma'lumot topilmadi")
        return render(request, f'book/file_search.html', {'search': search})

    return render(request, f'book/file_search.html', {'search': search})





def free_download(request):
    slug=request.POST.get('slug')
    ########
    fayl = File.objects.get(slug=slug)
    fayl.download_count+=1
    fayl.save()
    file_path2=request.POST.get('url2')
    user=request.POST.get('user2')
    print(user)
    file_path=f".{file_path2}"



    try:
        response = FileResponse(open(file_path, 'rb'))
        response['content_type'] = "application/octet-stream"
        response['Content-Disposition'] = 'attachment; filename=' + os.path.basename(file_path)
        return response
    except Exception:
        raise

def premium_download(request):
    slug=request.POST.get('slug')
    ########
    fayl = File.objects.get(slug=slug)
    fayl.download_count+=1
    fayl.save()

    ##############
    file_path2=request.POST.get('url2')
    file_path = f".{file_path2}"############file

    coin=int(request.POST.get('coin1'))#############
    user=User_coin.objects.get(user__username=request.user.username)

    print(user.coins,"  ",type(user.coins))
    print(coin,"  ",type(coin))

    if user.coins>=coin:
        user.coins=user.coins-coin
        print(user.coins)
        user.save()

        try:
            response = FileResponse(open(file_path, 'rb'))
            response['content_type'] = "application/octet-stream"
            response['Content-Disposition'] = 'attachment; filename=' + os.path.basename(file_path)
            return response
        except Exception:
            raise
    else:
        messages.error(request, "Sizda yetarlicha  tanga yo'q iltimos  ")
        messages.error(request, "Iltimos tangacha sotib oling  ")
        file = File.objects.get(slug=slug)

        data = {
            'name': file.name,
            'img': file.img.url,
            'count': file.download_count,
            'title': file.title,
            'file': file.file.url,
            'coin': file.coin,
            'slug':slug,
            'view':file.view

        }

        return render(request, 'book/file_detail.html', {'file': data})


