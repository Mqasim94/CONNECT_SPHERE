from django import forms
from .models import Share, Post

class SharePostForm(forms.ModelForm):
    class Meta:
        model = Share
        fields = ['reciever']

class CreateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'created_on', 'image', 'is_private']