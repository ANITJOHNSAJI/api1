from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.fun2,name='fun2'),
    path('fun3',views.fun3,name='fun3'),
    path('fun4/<int:d>',views.fun4,name='fun4'),
]
