from django.forms import ModelForm
from django import forms
from .models import Project, Tag


class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'description', 'image', 'git_url', 'tag']
        
        widgets = {
            'tag': forms.CheckboxSelectMultiple(),
        }
        
        
class TagForm(ModelForm):
    class Meta:
        model = Tag
        fields = ['name']