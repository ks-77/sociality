from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.forms import ModelForm

from accounts.models import CustomUser


class UserRegistrationForm(UserCreationForm):
    email_or_phone = forms.CharField(max_length=150, required=True, help_text="Enter your email or phone number")

    class Meta:
        model = CustomUser
        fields = ["username", "email_or_phone", "password1", "password2"]

    def clean_email_or_phone(self):
        email_or_phone = self.cleaned_data.get("email_or_phone")
        if "@" in email_or_phone:
            if CustomUser.objects.filter(email=email_or_phone).exists():
                raise forms.ValidationError("A user with that email already exists.")
            self.cleaned_data["email"] = email_or_phone
            self.cleaned_data["phone_number"] = None
        else:
            if CustomUser.objects.filter(phone=email_or_phone).exists():
                raise forms.ValidationError("A user with that phone number already exists.")
            self.cleaned_data["email"] = None
            self.cleaned_data["phone_number"] = email_or_phone
        return email_or_phone

    def save(self, commit=True):
        user = super().save(commit=False)
        user.username = self.cleaned_data["username"]
        user.email = self.cleaned_data.get("email")
        user.phone = self.cleaned_data.get("phone_number")
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(max_length=30, required=True)
    password = forms.CharField(max_length=150, required=True)

    class Meta:
        model = CustomUser
        fields = ["username", "password"]


class UserForm(ModelForm):
    email_or_phone = forms.CharField(max_length=150, required=True, help_text="Enter your email or phone number")

    class Meta:
        model = CustomUser
        fields = ["username", "email", "phone_number"]

    def clean_email_or_phone(self):
        email_or_phone = self.cleaned_data.get("email_or_phone")
        if "@" in email_or_phone:
            if CustomUser.objects.filter(email=email_or_phone).exists():
                raise forms.ValidationError("A user with that email already exists.")
            self.cleaned_data["email"] = email_or_phone
            self.cleaned_data["phone_number"] = None
        else:
            if CustomUser.objects.filter(phone_number=email_or_phone).exists():
                raise forms.ValidationError("A user with that phone number already exists.")
            self.cleaned_data["email"] = None
            self.cleaned_data["phone_number"] = email_or_phone
        return email_or_phone
