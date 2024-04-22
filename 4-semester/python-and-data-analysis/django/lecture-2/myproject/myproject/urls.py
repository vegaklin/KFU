from django.urls import path
from hello import views

urlpatterns = [path('products/<int:productid>/', views.products),
               path('users/', views.users), 
               ]