from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.utils import timezone
from django.views.generic import CreateView, DetailView, ListView, TemplateView

from accounts.forms import UserLoginForm, UserRegistrationForm
from accounts.models import CustomUser
from blog.models import Post, Story
from interactions.models import Subscription


class UserLoginView(LoginView):
    form_class = UserLoginForm
    template_name = "registration/login.html"
    success_url = reverse_lazy("index")

    def form_valid(self, form):
        return super(UserLoginView, self).form_valid(form)


class UserLogoutView(LogoutView):
    next_page = reverse_lazy("login")


class UserRegistrationView(CreateView):
    template_name = "registration/registration.html"
    form_class = UserRegistrationForm
    success_url = reverse_lazy("home")

    def form_valid(self, form):
        super().form_valid(form)
        user = form.save()
        login(self.request, user)
        return HttpResponseRedirect(self.get_success_url())


class HomePageView(LoginRequiredMixin, TemplateView):
    template_name = "common/home.html"

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        user = self.request.user
        following_users = Subscription.objects.filter(subscriber=user).values_list("author", flat=True)
        context["posts"] = Post.objects.filter(creator__in=following_users).order_by("-creation_date")

        current_time = timezone.now()
        context["stories"] = Story.objects.filter(creator__in=following_users, expire_date__gt=current_time).order_by(
            "-creation_date"
        )

        return context


class UserProfileView(LoginRequiredMixin, DetailView):
    model = CustomUser
    template_name = "user/profile.html"
    context_object_name = "user"

    def get_object(self, queryset=None):
        pk = self.kwargs.get("pk")
        return get_object_or_404(CustomUser, pk=pk)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.object
        context["posts"] = Post.objects.filter(creator=user).order_by("-creation_date")
        context["followers_count"] = self.object.subscribers.count()
        context["following_count"] = self.object.authors.count()
        context["posts_count"] = self.object.post.count()
        return context
