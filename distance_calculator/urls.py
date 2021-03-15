"""find_distance URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
# from django.contrib import admin
from distance_calculator import views     
from django.urls import path
from django.conf import settings

urlpatterns = [
    path('',views.CalculatorView.index, name='index'),
    path('calc',views.CalculatorView.calculator, name='calc'),
    path('calculator/', views.calculator_list),
    path('calculator/<int:pk>/', views.calculator_detail),
]