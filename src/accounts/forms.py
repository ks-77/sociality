from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm

from accounts.models import UserProfile


class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ["username", "email_or_phone", "password1", "password2"]


class UserForm(ModelForm):
    class Meta:
        model = get_user_model()
        fields = ["username", "email_or_phone"]


class UserProfileForm(ModelForm):
    class Meta:
        model = UserProfile
        exclude = ["user"]
        fields = "__all__"
