from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('register', views.register, name='register'),
    path('signin',views.signin, name='signin'),
    path('settings',views.settings, name='settings'),
    path('change',views.change, name='change'),
    path('cpw',views.cpw, name='cpw'),
    path('logout',views.logout, name='logout'),


    
     
]