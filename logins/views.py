from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.template import loader
from django.contrib.auth import login,logout
from django.contrib import messages
# Create your views here.
from django.contrib.auth.models import User
from django.conf import settings
from .forms import CustomUserCreationForm
from .models import *


def choose(request):
    return render(request,'logins/choose.html',{})


def index(request):
    return render(request,'logins/index.html',{})

def signup_view(request):
    if request.method=='POST':
        #form=CustomUserCreationForm(request.POST)#UserCreationForm(request.POST)
        #if form.is_valid():
            u = User.objects.create_user(
                request.POST['usernamee'],
                request.POST['emaill'],
                request.POST['passwordd1'],
            )
            s = SignupData()
            #user=form.save()
            #messages.success(request, 'Account created successfully')
            #login(request,user)
            s.user = u
            #rno=request.POST.get('rnum')#name='rnum'
            #author.rnum=rno
            s.first_name=request.POST.get('first_namee')
            s.last_name=request.POST.get('last_namee')
            s.user_type=request.POST.get('user_typee')
            s.phone_num=request.POST.get('phonee')
            s.save()
            return redirect('logins:login_view')
    else:
        form=CustomUserCreationForm(request.POST)#UserCreationForm()
    return render(request,'logins/signup_page.html',{'form':form})

def login_view(request):
    if request.method=='POST':
        form=AuthenticationForm(data=request.POST)
        if form.is_valid():
            user=form.get_user()
            login(request,user)
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect('events:index')
            #return render(request,'logins/login.html',{'name':user})

    else:
        form=AuthenticationForm()
    return render(request,'logins/login.html',{'form':form})

def logout_view(request):
    if request.method=='POST':
        logout(request)
        return redirect('events:index')
    else:
        return render(request,'logins/logout_page.html',{})

def landing_page(request):
    return render(request, 'accounts/index.html',{})
