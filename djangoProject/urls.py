"""djangoProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from myfirstproject.views import main, my_home, my_homepage, article, password, generate_password
from djangoProject import views


urlpatterns = [
    path('admin', main),
    # path('', main),
    path('home/', my_home),
    path('article/<int:article_id>/', article, name='article'),
    path('article/<int:article_id>/<slug:name>', article, name="article_name"),
    path('password/<slug:my_password>', password, name='my_password'),
    path('password/generate/<int:length>/', generate_password),
    path('', include('myfirstproject.urls')),
    path('', views.homepage1, name='homepage'),
    path('homepage.html', views.homepage1, name='homepage'),
    path('profile.html', views.profile1, name='profile')
]
