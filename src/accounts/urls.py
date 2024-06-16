from django.urls import path

from accounts.forms import UserRegistrationForm
from accounts.views import (UserLoginView, UserLogoutView, UserProfileView,
                            UserRegistrationView, create_student)

app_name = "accounts"

urlpatterns = [
    path("registration/", UserRegistrationView.as_view(), name="registration"),
    path("login/", UserLoginView.as_view(), name="login"),
    path("logout/", UserLogoutView.as_view(), name="logout"),
    path("profile/<int:pk>/", UserProfileView.as_view(), name="profile"),
    path("create-student/", create_student, name="create_student")
]
