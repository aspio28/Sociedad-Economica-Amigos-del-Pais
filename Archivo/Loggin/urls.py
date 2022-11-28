from django.contrib import admin
from django.urls import path, include
from . import views, search

urlpatterns = [
    path('', views.home, name="home"),
    path('SignUp', views.SignUp, name="SignUp"),
    path('SignIn', views.SignIn, name="SignIn"),
    path('LogOut', views.SignOut, name="LogOut"),
    path('Search', search.Search, name = "Search" )
]
