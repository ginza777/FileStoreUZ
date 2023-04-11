from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.models import User
from django.contrib import auth
from  django.contrib import  messages
from .forms import *
import requests
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect



def signup(request):
    messages.success(request,"""parol kamida 1 ta katta harf ,bitta belgi(! @ # $ % ^ & *  _ +) hamda kichik harflar va sonlardan iborat bo'lishi shart !!! """)
    if request.method == "POST":
        form = SignUpForm(request.POST)

        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
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
            messages.success(request, "tizimga kiring")

            return render(request, 'registration/signin.html')
        else:
            form = SignUpForm()
            messages.success(request, "nimadir xato")

            return render(request, 'registration/signup.html', {'form': form})
    return render(request, 'registration/signup.html')

def signout(request):
    logout(request)
    return redirect('books')

def signin(request):

    if request.method=="POST":
        email = request.POST['email']
        password = request.POST['password1']
        username = User.objects.get(email=email.lower()).username
        user=authenticate(username=username,password=password)

        if user is not None:
            login(request, user)
            user.is_active=True


            user.save()


            return redirect('books')
        else:
            messages.error(request,"qaytadan urinib ko'ring")
            return redirect('signin')
    return render(request,'registration/signin.html')




