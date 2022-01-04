from django.db import models
from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Post

# Create your views here.

# def home(request):
#     return HttpResponse('<h1> Callodine Blog </h1>')


# def about(request):
#     return HttpResponse('<h1> Profile - Baju </h1>')

# posts = [
#     {
#         'author':'Baju',
#         'username':'isribalaji',
#         'date_posted':'December 30, 2021',
#         'content':'Forcing ourselves or others to always be positive can be harmful to our well-being and our relationships. There is a better approach.'
#     },
#     {
#         'author':'Abhishek',
#         'username':'abhishekp',
#         'date_posted':'December 28, 2021',
#         'content':'I have 3 big surprises for you this new year, the first of which I will announce on Jan 1st. But can you guess without any hint from me'
#     },
#     {
#         'author':'Priya',
#         'username':'priyavarman',
#         'date_posted':'December 29, 2021',
#         'content':'What is your favorite movie of all time?'
#     }
# ]

## We are going to create class based views which will handle many things on their own at the backend. Previously, we have used function based views.


posts = Post.objects.all()

@login_required
def home(request):
    context = {
        'post' : posts,
        'title' : 'Happy Eve!!'
    }

    return render(request, 'microblog/home.html', context)

class PostView(LoginRequiredMixin, ListView):
    model = Post
    template_name = 'microblog/home.html'
    context_object_name = 'post'
    ordering = ['-date_posted']

class PostDetailView(LoginRequiredMixin, DetailView):
    model = Post

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title','content']

    def form_valid(self, form):
        form.instance.author = self.request.user.first_name
        form.instance.username = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title','content']

    def form_valid(self, form):
        form.instance.author = self.request.user.first_name
        form.instance.username = self.request.user
        return super().form_valid(form)

    def test_func(self):
        current_post = self.get_object()
        if(current_post.username == self.request.user):
            return True
        else:
            return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        current_post = self.get_object()
        if(current_post.username == self.request.user):
            return True
        else:
            return False

@login_required
def about(request):
    context = {
        'title':'isribalaji'
    }
    return render(request, 'microblog/about.html', context)

def error_404(request, *args, **argv):
        data = {}
        return render(request,'microblog/error404.html', data)

def error_500(request, *args, **argv):
        data = {}
        return render(request,'microblog/error500.html', data)