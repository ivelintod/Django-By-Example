from django import forms
from .models import Comment


class EmailPostFrom(forms.Form):
    name = forms.CharField(max_length=25)
    email = forms.EmailField()
    to = forms.EmailField()
    comments = forms.CharField(required=False,
                               widget=forms.Textarea)


class CommentPost(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')
