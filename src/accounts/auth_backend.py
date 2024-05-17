from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend
from django.db.models import Q

UserModel = get_user_model()


class CustomAuthBackend(ModelBackend):
    def authenticate(self, request, username=None, email=None, phone_number=None, password=None, **kwargs):
        UserModel = get_user_model()

        if not (username or email or phone_number) or not password:
            return None

        try:
            user = (
                UserModel._default_manager.get(Q(username=username))
                if username
                else (
                    UserModel._default_manager.get(Q(email=email))
                    if email
                    else UserModel._default_manager.get(Q(phone_number=phone_number))
                )
            )
        except UserModel.DoesNotExist:
            return None

        else:
            if user.check_password(password) and self.user_can_authenticate(user):
                return user
