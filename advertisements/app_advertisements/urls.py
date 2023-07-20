from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='/'),
    path('top-sell', top, name='top'),
    path('advertisement_',advertisement,name='advertisement_'),
    path('advertisement-post',advertisement_post,name='advertisement_post'),
    path('login',login,name='login'),
    path('profile',profile,name='profile'),
    path('register',register,name='register'),
]
"""
https://mysite.com/
"""