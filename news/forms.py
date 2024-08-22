from django import forms
from .models import NewsItem

class NewsItemForm(forms.ModelForm):
    class Meta:
        model = NewsItem
        fields = ['title', 'description', 'date', 'image', 'category', 'author', 'url']
