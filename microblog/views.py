from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
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

posts = Post.objects.all()

@login_required
def home(request):
    context = {
        'post' : posts,
        'title' : 'Happy Eve!!'
    }

    return render(request, 'microblog/home.html', context)


def about(request):
    context = {
        'title':'isribalaji'
    }
    return render(request, 'microblog/about.html', context)

