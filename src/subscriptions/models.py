from django.db import models

from accounts.models import UserProfile


class Subscription(models.Model):
    subscriber = models.ForeignKey(UserProfile, related_name="subscribers", on_delete=models.CASCADE)
    author = models.ForeignKey(UserProfile, related_name="authors", on_delete=models.CASCADE)
