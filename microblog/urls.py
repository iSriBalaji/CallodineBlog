from django.urls import path
from . import views
from .views import PostView,PostDetailView,PostCreateView,PostUpdateView, PostDeleteView

urlpatterns = [
    # path('', views.home, name='miniblog'),
    path('', PostView.as_view(), name='miniblog'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='individual_post'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post_update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),
    path('post/new/', PostCreateView.as_view(), name='new_post'),
    path('about/', views.about, name='profile'),
]