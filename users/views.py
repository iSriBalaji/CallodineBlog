from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import NewUser

# Create your views here.

def register(request):
    if(request.method == 'POST'):
        form = NewUser(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            first_name = form.cleaned_data.get('first_name')
            messages.success(request, f'We successfully added {first_name} to our Callodine family!')
            return redirect('login')
    else:
        form = NewUser()
    return render(request, 'users/register.html', {'form': form})

@login_required
def profile(request):
    return render(request, 'users/profile.html')