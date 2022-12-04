from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('Sign',views.Sign, name="Sign"),
    path('SignUp', views.SignUp, name="SignUp"),
    path('SignIn', views.SignIn, name="SignIn"),
    path('LogOut', views.SignOut, name="LogOut"),
]
