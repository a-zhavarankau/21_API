from .models import Department
from django.forms import ModelForm, TextInput
from .models import Department


class PostForm(ModelForm):
    class Meta:
        model = Department
        fields = '__all__'
        # widgets = {"name": TextInput(attrs={
        #     'class': 'form-control',
        #     'placeholder': "name"
        #     })
        # }

# class DepartmentForm(ModelForm):
#     class Meta:
#         model = Department
#         fields = ['name']
#         widgets = {"name": TextInput(attrs={
#             'class': 'form-control',
#             'placeholder': "name"
#             })
#         }

