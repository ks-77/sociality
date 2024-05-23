from django.contrib import admin

from blog.models import Post, Story

admin.site.register([Post, Story])
