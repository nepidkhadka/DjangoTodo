from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('addtodo/', views.addtodo, name="addtodo"),
    path('setdone/<int:id>', views.setdone, name="setdone"),
    path('delete/<int:id>', views.delete, name="delete")
]
