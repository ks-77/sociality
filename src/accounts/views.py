from django.contrib.auth import login
from django.contrib.auth.views import LoginView, LogoutView
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import CreateView

from accounts.forms import UserLoginForm, UserRegistrationForm
from accounts.models import CustomUser


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
