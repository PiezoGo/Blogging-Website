from django import forms
from .models import Comment, Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'excerpt', 'body', 'tags']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'brutalist-input'}),
            'excerpt': forms.Textarea(attrs={'class': 'brutalist-input', 'rows': 2}),
            'body': forms.Textarea(attrs={'class': 'brutalist-input', 'rows': 12}),
            'tags': forms.SelectMultiple(attrs={'class': 'brutalist-input'}),
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['body']
        widgets = {
            'body': forms.Textarea(attrs={
                'rows': 3,
                'placeholder': 'Write your comment...',
                'class': 'brutalist-input',
            }),
        }


class SearchForm(forms.Form):
    q = forms.CharField(
        required=False,
        max_length=100,
        widget= forms.TextInput(attrs={
            'placeholder': 'Search posts...',
            'class': 'brutalist-input',
        })
    )
