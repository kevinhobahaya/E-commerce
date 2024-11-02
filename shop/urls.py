from django.urls import path, include

from shop.views import * 

urlpatterns = [
    path('',indexPage, name= 'home'),
    path('<int:myid>',detail,name='detail'),
    path('checkout',checkout,name='checkout'),
    path('confirmation',confirmation,name='confirmation')
    
]