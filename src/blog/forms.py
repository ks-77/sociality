from django import forms
from django.forms import ModelForm

from blog.models import Post


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ["id", "creator", "media_file", "description", "location", "creation_date"]
