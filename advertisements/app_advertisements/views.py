from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request,'index.html')

def top(request):
    return render(request,'top-sellers.html')




# Create your views here.
