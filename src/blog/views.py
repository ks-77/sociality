from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy
from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  TemplateView)
from djoser.conf import User

from blog.forms import CreatePostForm, CreateStoryForm, PostForm
from blog.models import Post, Story
from blog.tasks import create_post_task, create_story_task
from core.forms import GenerationQuantityForm
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

        if "subscribe" in request.POST:
            subscription, created = Subscription.objects.get_or_create(subscriber=user, author=post.creator)
            if not created:
                subscription.delete()

        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return reverse_lazy("blog:post", kwargs={"pk": self.kwargs["pk"]})


class UserStoriesView(LoginRequiredMixin, ListView):
    model = Story
    template_name = "blog/story.html"
    context_object_name = "stories"
    paginate_by = 1

    def get_queryset(self):
        return Story.active().filter(creator=self.kwargs["pk"]).order_by("-creation_date")


class CreationPageView(LoginRequiredMixin, TemplateView):
    template_name = "creation/main-creation-page.html"


class StoryCreationView(LoginRequiredMixin, CreateView):
    template_name = "blog/create-story.html"
    form_class = CreateStoryForm

    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy("accounts:profile", kwargs={"pk": self.request.user.pk})


class PostCreationView(LoginRequiredMixin, CreateView):
    template_name = "blog/create-post.html"
    form_class = CreatePostForm

    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy("accounts:profile", kwargs={"pk": self.request.user.pk})


class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    template_name = "blog/delete-post.html"

    def get_queryset(self):
        return self.model.objects.filter(creator=self.request.user)

    def get_success_url(self):
        return reverse_lazy("accounts:profile", kwargs={"pk": self.request.user.pk})


class StoryDeleteView(LoginRequiredMixin, DeleteView):
    model = Story
    template_name = "blog/delete-story.html"

    def get_queryset(self):
        return Story.active().filter(creator=self.request.user)

    def get_success_url(self):
        return reverse_lazy("accounts:profile", kwargs={"pk": self.request.user.pk})


def create_story(request: HttpRequest) -> HttpResponse:
    message = None
    if request.method == "POST":
        form = GenerationQuantityForm(request.POST)
        if form.is_valid():
            quantity = form.cleaned_data["quantity"]
            create_story_task.delay(quantity)
            message = "TASK STARTED, creating stories"
    else:
        form = GenerationQuantityForm()
    return render(request, "generate/general_generation(del).html", {"form": form, "message": message})


def create_post(request: HttpRequest) -> HttpResponse:
    message = None
    if request.method == "POST":
        form = GenerationQuantityForm(request.POST)
        if form.is_valid():
            quantity = form.cleaned_data["quantity"]
            create_post_task.delay(quantity)
            message = "TASK STARTED, creating posts"
    else:
        form = GenerationQuantityForm()
    return render(request, "generate/general_generation(del).html", {"form": form, "message": message})
