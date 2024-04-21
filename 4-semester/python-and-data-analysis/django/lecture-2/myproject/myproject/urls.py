from django.contrib import admin
from django.urls import path
from hello import views

urlpatterns = [path(r'^about/contact/', views.contact),
               path(r'^about', views.about), 
               path('', views.index),
               ]