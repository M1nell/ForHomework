from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import advertisement
from .forms import AdvertisementForm
from django.urls import reverse

def index(request):
    advertisements = advertisement.objects.all()
    context = {'advertisements':advertisements}
    return render(request,'advertisements/index.html',context = context)

def top(request):
    return render(request,'advertisements/top-sellers.html')

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
    return render(request, 'advertisements/advertisement-post.html', context=context)



def advertisements(request):
    return render(request,'advertisements/advertisement.html')




# Create your views here.
