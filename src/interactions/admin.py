from django.contrib import admin

from interactions.models import Comment, Like, Subscription

admin.site.register([Subscription, Like, Comment])
