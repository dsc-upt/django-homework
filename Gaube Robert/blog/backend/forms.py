from django import forms
from .models import Article

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = "__all__"
        labels = {
            "title": "Article Title",
            "description": "Article Description",
            "User": "The owner"
        }
