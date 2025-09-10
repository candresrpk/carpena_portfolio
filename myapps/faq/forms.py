from django.forms import ModelForm
from .models import Faq, Tag, Faq_tag, Faq_detail
from django import forms

class FaqForm(ModelForm):
    class Meta:
        model = Faq
        fields = ['question', 'detail', 'tag']
        
        widgets = {
            'tag': forms.CheckboxSelectMultiple(),
        }
        

class tagForm(ModelForm):
    class Meta:
        model = Tag
        fields = ['name']
        

class FaqDetailForm(ModelForm):
    class Meta:
        model = Faq_detail
        fields = ['title', 'content', 'order', 'code', 'code_type']

        
        
        