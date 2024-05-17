import re

from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _


def validate_email_or_phone(value):
    if not re.match(r"^(\+\d{1,3}[- ]?)?\d{10}$|^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$", value):
        raise ValidationError(_("Invalid email or phone number format"))


def validate_username(value):
    if 1 <= len(value) <= 20 and value.replace("_", "").isalnum():
        return True
    raise ValidationError(
        _("Username must be between 1 and 20 characters and contain only letters, numbers, and underscores")
    )


def validate_name(value):
    if not re.match("^[a-zA-Z]*$", value):
        raise ValidationError(_("Name must contain only letters"))
    if len(value) > 50:
        raise ValidationError(_("Name must be at most 50 characters long"))
