from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy
from django.utils import timezone
from django.views.generic import (CreateView, DetailView, ListView,
                                  TemplateView, UpdateView)

from accounts.forms import (UserForm, UserLoginForm, UserProfileForm,
                            UserRegistrationForm)
from accounts.models import CustomUser
from accounts.tasks import create_user_task
from blog.models import Post, Story
from core.forms import GenerationQuantityForm
from interactions.models import Subscription


class UserLoginView(LoginView):
    form_class = UserLoginForm
    template_name = "registration/login.html"
    success_url = reverse_lazy("index")

    def form_valid(self, form):
        return super(UserLoginView, self).form_valid(form)


class UserLogoutView(LogoutView):
    next_page = reverse_lazy("accounts:login")


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

    def post(self, request, *args, **kwargs):
        author = self.get_object()

        subscription, created = Subscription.objects.get_or_create(subscriber=request.user, author=author)
        if not created:
            subscription.delete()

        return HttpResponseRedirect(self.get_success_url())

    def get_object(self, queryset=None):
        pk = self.kwargs.get("pk")
        return get_object_or_404(CustomUser, pk=pk)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        author = self.object
        user = self.request.user
        context["posts"] = Post.objects.filter(creator=author).order_by("-creation_date")
        context["followers_count"] = self.object.authors.count()
        context["following_count"] = self.object.subscribers.count()
        context["posts_count"] = self.object.post.count()
        context["is_subscribed"] = Subscription.objects.filter(subscriber=user, author=author).exists()
        return context

    def get_success_url(self):
        return reverse_lazy("accounts:profile", kwargs={"pk": self.kwargs["pk"]})


class UpdateUserProfileView(LoginRequiredMixin, UpdateView):
    form_class = UserProfileForm
    model = CustomUser
    template_name = "user/profile-edit.html"

    def get_object(self, queryset=None):
        pk = self.kwargs.get("pk")
        return get_object_or_404(CustomUser, pk=pk)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        self.object = form.save()
        return HttpResponseRedirect(self.get_success_url())

    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(form=form))

    def get_success_url(self):
        return reverse_lazy("accounts:profile", kwargs={"pk": self.kwargs["pk"]})


def create_student(request: HttpRequest) -> HttpResponse:
    message = None
    if request.method == 'POST':
        form = GenerationQuantityForm(request.POST)
        if form.is_valid():
            quantity = form.cleaned_data['quantity']
            for _ in range(quantity):
                create_user_task.delay()
            message = "TASK STARTED, creating students"
    else:
        form = GenerationQuantityForm()
    return render(request, 'generate/general_generation(del).html', {'form': form, 'message': message})
