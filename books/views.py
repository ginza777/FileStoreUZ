from django.http import HttpResponse, Http404, StreamingHttpResponse, FileResponse
from django.shortcuts import render,redirect
from django.contrib import messages

from .models import Books
from operator import  itemgetter
from blogs.models import Blog
from django.db.models import Q
from adminpanel.models import  Contact,Search_Book
from django.conf import settings
import os
from django.conf import settings
from users.models import User_coin



########################
# Create your views here.

def books(request):
    books=Books.objects.all()
    last_book=books.order_by("created_data")[::-1]
    data_new=[]
    data_bar=[]
    data=books.order_by("download_count")
    data_trend=[]





    for book in data:
        i = {
            'name': book.name,
            'img': book.img.url,
            'count': book.download_count,
            'slug': book.slug,
            'view':book.view,
            'star':book.star

        }

        data_trend.append(i)

        count=0

        for book in last_book:
            i={
                'name':book.name,
                'img':book.img.url,
                'count':book.download_count,
                'slug':book.slug,


            }
            data_new.append(i)

            if count<7:
                data_bar.append(i)
            else:continue

            count+=1

    datax=sorted(data_new, key=lambda  d:d['name'],reverse=True)

    ####################blog
    blogs=Blog.objects.all()

        ######################Contact

    contact=Contact.objects.last()



    return render(request,'book/home.html',{'books':data_trend,'data_new':data_new,'data_bar':data_bar,'data_new2':datax,'blogs':blogs,'contact':contact})


def book_detail(request,slug):
    book=Books.objects.get(slug=slug)
    book.view+=1
    book.save()



    data={
        'name': book.name,
        'img': book.img.url,
        'count': book.download_count,
        'title':book.title,
        'file': book.file.url,
        'coin':book.coin,
        'slug':slug,
        'view':book.view



    }

    return render(request,'book/file_detail.html',{'data':data})


def search_books(request):
    search = request.POST.get('search')

    if search:
        if Search_Book.objects.filter(text=search):

            a = Search_Book.objects.get(text=search)
            a.count_search += 1
            a.save()


        else:
            Search_Book.objects.create(text=search).save()


        search_book =Books.objects.filter(Q(tag__contains=search))


        data_book = []
        for book in search_book:

            context = {
                'name': book.name,
                'img': book.img.url,
                'count': book.download_count,
                'slug': book.slug,


            }
            data_book.append(context)
        return render(request, 'book/index.html', {'search_books': data_book,'search':search})

    return render(request,f'book/index.html',{'search':search})

def free_download(request):
    slug = request.POST.get('slug')
    book = Books.objects.get(slug=slug)
    book.download_count+=1

    book.save()

    file_path2=request.POST.get('url1')
    user = request.POST.get('user1')
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
    book=Books.objects.get(slug=slug)
    book.download_count+=1
    book.save()


    file_path2=request.POST.get('url1')
    file_path = f".{file_path2}"############file
    user2 = request.POST.get('user1')
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
        book = Books.objects.get(slug=slug)

        data = {
            'name': book.name,
            'img': book.img.url,
            'count': book.download_count,
            'title': book.title,
            'file': book.file.url,
            'coin': book.coin,
            'slug':slug

        }

        return render(request, 'book/file_detail.html', {'data': data})
























































# def download(request,path):
#
#
# 	file_path=os.path.join(settings.MEDIA_ROOT,path)
# 	if os.path.exists(file_path):
#
# 		with open(file_path,"rb") as fh:
# 			response=HttpResponse(fh.read(),content_type="application/book")
# 			response['Content-Disposition']='inline;filename='+os.path.basename(file_path)
#
# 			return  response
