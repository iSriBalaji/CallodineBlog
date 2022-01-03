from django.urls import path
from . import views
from .views import PostView

urlpatterns = [
    path('', views.home, name='miniblog'),
    path('about/', views.about, name='profile'),
]