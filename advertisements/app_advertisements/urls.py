from django.urls import path
from .views import index, top

urlpatterns = [
    path('', index, name='/'),
    path('top-sell', top, name='top'),
]
"""
https://mysite.com/
"""