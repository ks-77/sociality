from django import forms
from django.forms import ModelForm

from interactions.models import Comment


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ["content"]
        widgets = {
            "content": forms.Textarea(attrs={"class": "form-control", "rows": 3, "placeholder": "Leave a comment..."}),
        }
