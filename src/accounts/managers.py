from django.contrib.auth.models import UserManager


class CustomUserManager(UserManager):
    def _create_user(self, username, email_or_phone, password, **extra_fields):
        if not email_or_phone:
            raise ValueError("The email or phone number must be set")

        if "@" in email_or_phone:
            email = email_or_phone
            phone_number = None
        else:
            email = None
            phone_number = email_or_phone

        user = self.model(
            username=username, email=self.normalize_email(email), phone_number=phone_number, **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, email_or_phone=None, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)

        return self._create_user(username, email_or_phone, password, **extra_fields)

    def create_superuser(self, username, email_or_phone=None, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if not extra_fields.get("is_staff"):
            raise ValueError("Superuser must have is_staff=True.")
        if not extra_fields.get("is_superuser"):
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user(username, email_or_phone, password, **extra_fields)
