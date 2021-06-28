# import form class from django
from django import forms
  
# import GeeksModel from models.py
from .models import BlogModel
  
# create a ModelForm
class BlogForm(forms.ModelForm):
    # specify the name of model to use
    class Meta:
        model = BlogModel
        fields = "__all__"