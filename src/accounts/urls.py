from django.urls import path

from accounts.forms import UserRegistrationForm
from accounts.views import (UpdateUserProfileView, UserLoginView,
                            UserLogoutView, UserProfileView,
                            UserRegistrationView, create_student)

app_name = "accounts"

urlpatterns = [
    path("registration/", UserRegistrationView.as_view(), name="registration"),
    path("login/", UserLoginView.as_view(), name="login"),
    path("logout/", UserLogoutView.as_view(), name="logout"),
    path("profile/<int:pk>/", UserProfileView.as_view(), name="profile"),
    path("profile-edit/<int:pk>/", UpdateUserProfileView.as_view(), name="profile_update"),
    path("create-student/", create_student, name="create_student"),
]
