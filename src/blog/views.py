from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, render
from django.views.generic import DetailView

from blog.forms import PostForm
from blog.models import Post


class PostDetailView(LoginRequiredMixin, DetailView):
    model = Post
    template_name = "blog/post.html"
    context_object_name = "post"
