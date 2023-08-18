from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import advertisement
from .forms import AdvertisementForm
from django.urls import reverse

def index(request):
    advertisements = advertisement.objects.all()
    context = {'advertisements':advertisements}
    return render(request,'index.html',context = context)

def top(request):
    return render(request,'top-sellers.html')

def advertisement_post(request):
    if request.method == "POST":
        form =AdvertisementForm(request.POST, request.FILES)
        if form.is_valid():
            advertisements = advertisement(**form.cleaned_data)
            advertisements.User = request.user
            advertisements.save()
            url = reverse('/')
            return redirect(url)
    else:
        form = AdvertisementForm()
    context = {'form': form}
    return render(request, 'advertisement-post.html', context=context)

def login(request):
    return render(request,'login.html')

def profile(request):
    return render(request,'profile.html')

def register(request):
    return render(request,'register.html')

def advertisements(request):
    return render(request,'advertisement.html')




# Create your views here.
