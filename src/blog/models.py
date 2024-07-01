from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from location_field.models.plain import PlainLocationField

from accounts.models import CustomUser


class Post(models.Model):
    creator = models.ForeignKey(CustomUser, related_name="post", on_delete=models.CASCADE)
    media_file = models.FileField(upload_to="blog/posts/")
    description = models.CharField(max_length=150, blank=True, null=True)
    location = PlainLocationField(based_fields=["city"], zoom=7, blank=True, null=True)
    creation_date = models.DateTimeField(_("creation date"), default=timezone.now)


class Story(models.Model):
    creator = models.ForeignKey(CustomUser, related_name="story", on_delete=models.CASCADE)
    media_file = models.FileField(upload_to="blog/stories/")
    location = PlainLocationField(based_fields=["city"], zoom=7, blank=True, null=True)
    creation_date = models.DateTimeField(_("creation date"), default=timezone.now)
    expire_date = models.DateTimeField(_("expire date"), blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.expire_date:
            self.expire_date = self.creation_date + timezone.timedelta(days=1)
        super().save(*args, **kwargs)

    @staticmethod
    def active():
        return Story.objects.filter(expire_date__gt=timezone.now())
