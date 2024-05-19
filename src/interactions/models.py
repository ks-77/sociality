from django.db import models

from accounts.models import CustomUser
from blog.models import Post


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    content = models.CharField(max_length=150, blank=True, null=True)


class Like(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)


class Subscription(models.Model):
    subscriber = models.ForeignKey(CustomUser, related_name="subscribers", on_delete=models.CASCADE)
    author = models.ForeignKey(CustomUser, related_name="authors", on_delete=models.CASCADE)
