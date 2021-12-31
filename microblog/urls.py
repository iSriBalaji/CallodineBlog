from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='miniblog'),
    path('about/', views.about, name='profile'),
]