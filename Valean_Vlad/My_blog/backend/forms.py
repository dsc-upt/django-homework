from django import forms
from .models import Article


class ArticleForm(forms.ModelForm):
    title = forms.CharField(label='', max_length=120, widget=forms.TextInput(attrs={"placeholder": "Article title"}))
    content = forms.CharField(widget=forms.Textarea(attrs={
        "placeholder": "Article content",
        "rows": 12,
        "cols": 150,
    }))

    class Meta:
        model = Article
        fields = [
            'title',
            'content',
        ]
