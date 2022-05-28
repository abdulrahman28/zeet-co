from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('sum',views.sum, name='sum'),
    path('signin', views.signin, name='signin'),
]