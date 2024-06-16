from django.urls import path

from interactions.views import create_like, create_comment, create_subscription

app_name = 'interactions'

urlpatterns = [
    path("create-like/", create_like, name="create-like"),
    path("create-comment/", create_comment, name="create-like"),
    path("create-subscription/", create_subscription, name="create-like"),
]
