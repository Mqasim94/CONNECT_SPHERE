from django import forms
from .models import Share

class SharePostForm(forms.ModelForm):
    class Meta:
        model = Share
        fields = ['post', 'receiver']