from django.contrib import admin
from django.urls import path
from store import views
urlpatterns = [
 
    path('', views.Index.as_view(),name='mainpage'),
    path('about/', views.about),
    path('home/', views.home),
    path('contact/', views.contact),
    path('signup/', views.signup),
    path('login/', views.Login.as_view(),name="login"),
    path('logout/', views.logout),
    path('cart/', views.cart,name="cart"),
    path('my_order/', views.my_order,name="order"),
    path('checkout', views.checkout.as_view(),name="checkout"),
    
  
]