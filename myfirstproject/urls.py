from django.urls import path
from djangoProject.views import *


urlpatterns = [
    path('profile', profile1, name='profile1'),
    path('product', product1, name='product1'),
    path('apple', apple1, name='apple1'),
    path('milk', milk1, name='milk1'),
    path('fish', fish1, name='fish1'),
    path('homepage', homepage1, name='homepage1')
]
