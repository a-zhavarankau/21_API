from django.forms import ModelForm, TextInput
from .models import *


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