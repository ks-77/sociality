from django.contrib.auth import get_user_model
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext as _

from accounts.managers import CustomUserManager
from core.utils.validators import (validate_email_or_phone, validate_name,
                                   validate_username)

gender = (
    ("Male", "Male"),
    ("Female", "Female"),
    ("Prefer not to say", "Prefer not to say"),
)


class CustomUser(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(unique=True, max_length=30, verbose_name=_("username"), validators=[validate_username])
    email = models.EmailField(
        unique=True, verbose_name=_("email"), null=True, blank=True, validators=[validate_email_or_phone]
    )
    phone_number = models.CharField(
        unique=True,
        max_length=20,
        verbose_name=_("phone number"),
        null=True,
        blank=True,
        validators=[validate_email_or_phone],
    )

    is_staff = models.BooleanField(
        _("staff status"),
        default=False,
        help_text=_("Designates whether the user can log into this admin site."),
    )

    is_active = models.BooleanField(
        _("active"),
        default=True,
        help_text=_(
            "Designates whether this user should be treated as active. " "Unselect this instead of deleting accounts."
        ),
    )
    date_joined = models.DateTimeField(_("date joined"), default=timezone.now)

    objects = CustomUserManager()

    EMAIL_FIELD = "email"
    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = [username]

    class Meta:
        verbose_name = _("custom_user")
        verbose_name_plural = _("custom_users")

    def clean(self):
        super().clean()

        if self.email:
            self.email = self.__class__.objects.normalize_email(self.email)


class UserProfile(models.Model):
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE, related_name="user_profile")
    avatar = models.ImageField(upload_to="avatars/users/", default="avatar/default.jpg")
    name = models.CharField(max_length=50, blank=True, null=True, validators=[validate_name])
    bio = models.CharField(max_length=150, blank=True, null=True)
    date_of_birth = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=20, choices=gender, blank=True, null=True)
    pronouns = models.CharField(max_length=20, blank=True, null=True)
    links = models.URLField(null=True, blank=True)
