from django import forms
from django.forms import ModelForm

from blog.models import Post, Story


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ["id", "creator", "media_file", "description", "location", "creation_date"]


class CreatePostForm(ModelForm):
    class Meta:
        model = Post
        fields = ["media_file", "description", "location"]


class CreateStoryForm(ModelForm):
    class Meta:
        model = Story
        fields = ["media_file", "location"]
