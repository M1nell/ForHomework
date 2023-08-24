from django.urls import path
from .views import *

urlpatterns = [
    path('login/',login,name='login'),
    path('profile/',profile,name='profile'),
    path('register/',register,name='register'),
    path('logout/',logout_vi, name = 'logout')
]