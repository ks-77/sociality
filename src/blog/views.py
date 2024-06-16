from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect, HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy
from django.views.generic import DetailView

from blog.forms import PostForm
from blog.models import Post
from blog.tasks import create_story_task, create_post_task
from interactions.forms import CommentForm
from interactions.models import Like, Subscription


class PostDetailView(LoginRequiredMixin, DetailView):
    model = Post
    template_name = "blog/post.html"
    context_object_name = "post"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = self.get_object()
        user = self.request.user
        context["form"] = CommentForm()
        context["like_count"] = self.object.likes.count()
        context["comment_count"] = self.object.comments.count()
        context["is_subscribed"] = Subscription.objects.filter(subscriber=user, author=post.creator).exists()
        return context

    def post(self, request, *args, **kwargs):
        post = self.get_object()
        user = self.request.user

        if "like" in request.POST:
            like, created = Like.objects.get_or_create(user=request.user, post=post)
            if not created:
                like.delete()

        if "content" in request.POST:
            form = CommentForm(request.POST)
            if form.is_valid():
                comment = form.save(commit=False)
                comment.user = request.user
                comment.post = post
                comment.save()

        subscription, created = Subscription.objects.get_or_create(subscriber=user, author=post.creator)
        if not created:
            subscription.delete()

        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return reverse_lazy("blog:post", kwargs={"pk": self.kwargs["pk"]})


def create_story(request: HttpRequest) -> HttpResponse:
    create_story_task.delay()
    return HttpResponse("TASK STARTED, creating a story")


def create_post(request: HttpRequest) -> HttpResponse:
    create_post_task.delay()
    return HttpResponse("TASK STARTED, creating a post")
