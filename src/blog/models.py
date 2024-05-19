from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from location_field.models.plain import PlainLocationField

from accounts.models import CustomUser


class Post(models.Model):
    creator = models.ForeignKey(CustomUser, related_name="post_creators", on_delete=models.CASCADE)
    media_file = models.FileField(upload_to="blog/")
    description = models.CharField(max_length=150, blank=True, null=True)
    location = PlainLocationField(based_fields=["city"], zoom=7, blank=True, null=True)
    creation_date = models.DateTimeField(_("creation date"), default=timezone.now)


class Story(models.Model):
    creator = models.ForeignKey(CustomUser, related_name="story_creators", on_delete=models.CASCADE)
    media_file = models.FileField(upload_to="stories/")
    location = PlainLocationField(based_fields=["city"], zoom=7, blank=True, null=True)
    creation_date = models.DateTimeField(_("creation date"), default=timezone.now)
