from django.contrib import admin
from django.urls import path,include
from .views import *
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('' , index, name="index"),   
    path('send_email/' ,  send_to_email , name="send_to_email"),

   

]



