from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth.models import User, auth
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required(login_url='login')
def home(request):
    return render(request, 'home.html')
def signup(request):
    if request.method == 'POST':
        username=request.POST['username']
        email=request.POST['email']
        password1=request.POST['password1']
        password2=request.POST['password2']
        
        if password1!=password2:
            return HttpResponse('password not matching! try again')
        elif User.objects.filter(username=username).exists():
            return HttpResponse('username already taken! try another username')
        else:
            user=User.objects.create_user(username=username,email=email,password=password1)
            user.save()
            return redirect('login')
        
    return render(request, 'signup.html')
def login(request):
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['pass']
        
        user=auth.authenticate(request,username=username,password=password)
        
        if user is not None:
            auth.login(request,user)
            return redirect('home')
        else:
            return HttpResponse('invalid credentials! try again')
    return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('login')