from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout as login_dj
from django.contrib.auth.decorators import login_required
from django.urls import reverse, reverse_lazy

def login(request):
    redirect_url = reverse('profile')
    if request.method == "GET":
        if request.user.is_authenticated:
            return redirect(redirect_url)
        else:
            return render(request,'app_auth/login.html')
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auntificate(request, username = username, password = password)
        if user is not None:
            login_dj(request,user)
            return redirect(redirect_url)
    return render(request,'app_auth/login.html', context={'error':"Error in this field(s)"})

@login_required(login_url= reverse_lazy('login'))
def profile(request):
    return render(request,'app_auth/profile.html')

def register(request):
    return render(request,'app_auth/register.html')

def logout_vi(request):
    logout(request)
    return redirect(reverse('login'))