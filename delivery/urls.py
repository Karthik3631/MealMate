from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('signIn/', views.signIn, name='signIn'),
    path('signUp/', views.signUp, name='signUp'),
    path('osignUp/',views.osignUp, name='osignUp'),
    path('osignIn/',views.osignIn,name='osignIn'),
    path('add_restaurant/',views.add_restaurant,name='add_restaurant'),
    path('show_restaurants/', views.show_restaurant, name='show_restaurant'),
]
