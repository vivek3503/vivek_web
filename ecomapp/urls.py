"""
URL configuration for mynewproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
 path('',views.index,name= 'index'),
 path('index_2/',views.index_2,name= 'index_2'),
 path('about/',views.about,name= 'about'),
 path('cart/',views.cart,name= 'cart'),
 path('checkout/',views.checkout,name= 'checkout'),
 path('contact/',views.contact,name= 'contact'),
 path('news/',views.news,name= 'news'),
 path('shop/',views.shop,name= 'shop'),
 path('login/', views.login, name='login'),
 path('logout/', views.logout, name= 'logout'),
 path('register/', views.register,name= 'register'),
 path('forget_password', views.forget_password, name='forget_password'),
 path('confirm', views.confirm, name= 'confirm'),
 path('add_to_cart/<str:id>', views.add_to_cart, name= 'add_to_cart'),
 path('remove/<str:id>',views.remove,name='remove'),
 path('cart_minus/<str:id>',views.cart_minus,name='cart_minus'),
 path('cart_plus/<str:id>',views.cart_plus,name='cart_plus'),

 
]
