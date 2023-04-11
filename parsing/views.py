from django.shortcuts import render,redirect
import json
from django.http import JsonResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import auth
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect
import requests
from bs4  import BeautifulSoup
from  django.contrib import  messages
from .forms import *
# Create your views here.
# def HomePageView(request):
#     return render(request,'index.html')
# def BlogPageView(request):
#     return render(request,'blog.html')
# def FilePageView(request):
#     return render(request, 'fayllar.html')


import random
import string
import os
import shutil




def SignPageView(request):
    messages.success(request,"""parol kamida 1 ta katta harf ,bitta belgi(! @ # $ % ^ & *  _ +) hamda kichik harflar va sonlardan iborat bo'lishi shart !!! """)
    return render(request, 'registration/signup.html')
def BookPageView(request):


    return render(request,'../../filestore/templates/book/home.html')






################################################################################3
def FilePageView(request):
    return render(request,'../../filestore/templates/book/files.html')



def FileSearch(request):
    if request.method=="POST":



        str2 = request.POST.get('search')
        #################link taxlash
        str3=str2.split()
        str4=f"""{str3[0]}"""
        l=len(str3)
        for i in range(1,l):
            str4=str4+f"""+{str3[i]}"""

       ##################################

        url="""https://fayllar.org/?q="""
        url=url+str4


        page = requests.get(f"""{url}""")
        bsoup = BeautifulSoup(page.content, 'html.parser')

        fayl= bsoup.find('table',class_="list5").findAll('tr',valign="top")




        data = []
        for i in fayl:

            link=f"""https://fayllar.org/"""+i.find('a').get('href')
            title=i.find('img').get('alt')
            font=i.find('font').text

            file={
                'title':title,
                'link':link,
                'font':font,
            }
            data.append(file)

        return render(request, '../../filestore/templates/book/files.html', { 'search': str2,'files':data})
def Clone():

        letters = string.ascii_letters
        x = "".join(random.sample(letters, 20))
        y = "".join(random.sample(letters, 20))
        orginal_name = """fayllar/Admission Guide For International Applicants (2).pdf"""
        copy_name = """fayllar/newfile.pdf"""
        new_name = f"""fayllar/{x + y}.pdf"""

        shutil.copy(orginal_name, copy_name)
        os.rename(copy_name, new_name)

        return new_name


    #
    #
    # except FileNotFoundError:
    #     print("The 'docs' directory does not exist")





def FileDownload(request):
    if request.method=="POST":

        url=request.POST.get('download')


        page2 = requests.get(f"""{url}""")
        bsoup2 = BeautifulSoup(page2.content, 'html.parser')
        title = bsoup2.find('div', class_="inside block-content").findNext('h1').text
        download1=bsoup2.find('div',class_="but3 rad").findNext('a').get('href')
        file_name=Clone()


        url2=f"""https://fayllar.org"""+download1
        page3=requests.get(f"""{url2}""")

        bsoup3=BeautifulSoup(page3.content,'html.parser')
        actions=bsoup3.find('form',enctype="multipart/form-data").__getitem__('action')

        url3=f"""https://fayllar.org"""+actions
        print(url3)

        files={'file-upload' : (file_name, open(file_name, 'rb'), 'text/plain')}
        data = {'_token': '', 'input-data': '', 'query-sig2': ''}

        request2=requests.post(url3,files=files,data=data)















    return render(request=request, template_name='../../filestore/templates/book/file_detail.html', context={'title': title ,'link':'#'})


#
# def Download(request):
#     if request.method=="POST":





























def SearchBook(request):
    if request.method=="POST":


        str=request.POST.get('search')



        page = requests.get(f"""https://www.pdfdrive.com/search?q={str}&pagecount=&pubyear=&searchin=&em=""")
        bsoup = BeautifulSoup(page.content, 'html.parser')

        book= bsoup.find(class_='files-new')
        # file_info=book.find(class_='file-info')
        # info=file_info.find_all('span')
        list=book.find_all('li')





        books=[]






        for i in list:


            img=i.findNext('img')
            info=i.find(class_='file-info')

            # link  qismi downloaD
            link=i.findNext('div' ,class_="file-left").find('a').get('href')




            link='https://www.pdfdrive.com'+link

            page2 = requests.get(f"""{link}""")
            bsoup2 = BeautifulSoup(page2.content, 'html.parser')
            download_link = bsoup2.find('span',id="download-button").findNext('a').get('href')

            download_link="""https://www.pdfdrive.com"""+f"""{download_link}"""


            ###############download










            # print(img['src'])
            # print(img['title'])
            # print(info)



            kitob={
                'img':img['src'],
                'title':img['title'],
                'link':download_link


            }
            books.append(kitob)




        return render(request,'../../filestore/templates/book/home.html',{'books':books,'search':str})


def Register(request ):
    if request.method=="POST":
        form = SignUpForm(request.POST)


        username=request.POST['username']
        email=request.POST['email']
        password1=request.POST['password1']
        password2=request.POST['password2']
        print(f"""
        name:  {username}\n
        email:  {email}\n
        password1:   {password1}\n
        password2:  {password2}\n """)

        if form.is_valid():
            user = form.save()
            user.refresh_from_db()

            user.is_active = True
            user.save()
            messages.success(request,"tizimga kiring")


            return render(request, 'registration/signin.html')
        else:
            form = SignUpForm()
            messages.success(request,"nimadir xato")


            return render(request,'registration/signup.html',{'form':form})










    return render(request,'registration/signup.html')


def LoginPageView(request):
    return render(request, 'registration/signin.html')




def Login(request):
    email = request.POST['email']
    password = request.POST['password1']
    print(email)
    print(password)
    if request.method=="POST":
        email = request.POST['email']
        password = request.POST['password1']
        username = User.objects.get(email=email.lower()).username
        user=authenticate(username=username,password=password)

        if user is not None:
            login(request, user)
            user.is_active=True


            user.save()


            return redirect('book')
        else:
            messages.error(request,"qaytadan urinib ko'ring")
            return redirect('login')








        # if form.is_valid():
        #     user = form.save()
        #     user.refresh_from_db()
        #
        #     user.is_active = True
        #     user.save()
        #     messages.success(request,"Saytga xush kelibsiz !!!")
        #
        #
        #     return render(request, 'book/home.html')
        # else:
        #     form = SignUpForm()
        #
        #     messages.success(request,"nimadir xato22")







    return render(request, 'registration/signin.html')


def signout(request):
    logout(request)
    return redirect('book')








