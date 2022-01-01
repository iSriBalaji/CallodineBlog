from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import fields


## In meta class we have to mention the model that the form is going to interact. Here it's User
## Meta gives us a nested namespace for configurations and keeps everything in one place
class NewUser(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)

    class Meta:
        model = User
        fields = ['first_name','last_name','username','email','password1','password2']