from django.db import models

from accounts.models import UserProfile
from posts.models import Post


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    content = models.CharField(max_length=150, blank=True, null=True)
