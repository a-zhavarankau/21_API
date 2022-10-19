from django import forms
from django.forms import ModelForm, TextInput
from .models import *
# from django.contrib.auth import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class PostForm(ModelForm):
    class Meta:
        model = Department
        fields = '__all__'


class EmplForm(ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'


class ProjForm(ModelForm):
    class Meta:
        model = Project
        fields = '__all__'


class RegisterUserForm(UserCreationForm):
    # In Django ONLY FOR(!) Registration don't work widgets in: class Meta: widgets = {...}
    # We need to specify every field itself with variable. If we not specify, it will be default "raw" html page.
    username = forms.CharField(label='login', widget=forms.TextInput(attrs={'class': 'form-input'}))
    email = forms.EmailField(label='e-mail', widget=forms.EmailInput(attrs={'class': 'form-input'}))
    password1 = forms.CharField(label='password', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    password2 = forms.CharField(label='confirm_password', widget=forms.PasswordInput(attrs={'class': 'form-input'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')   # F12 and inspect input field names


