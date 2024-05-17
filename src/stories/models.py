from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from location_field.forms.plain import PlainLocationField

from accounts.models import UserProfile


class Story(models.Model):
    creator = models.ForeignKey(UserProfile, related_name="story_creators", on_delete=models.CASCADE)
    media_file = models.FileField(upload_to="stories/")
    location = PlainLocationField(based_fields=["city"], zoom=7, blank=True, null=True)
    creation_date = models.DateTimeField(_("creation date"), default=timezone.now)
