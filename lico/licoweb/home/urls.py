from django.contrib import admin
from django.urls import path
from home import views


urlpatterns = [
   path("", views.index, name='home'),
   path("filefun", views.filefun, name='filefun'),
   path("createapp", views.createapp, name='createapp')
]
