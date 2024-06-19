from django.urls import path

from blog.views import PostDetailView, create_post, create_story

app_name = "blog"

urlpatterns = [
    path("post/<int:pk>/", PostDetailView.as_view(), name="post"),
    path("create-story/", create_story, name="create_story"),
    path("create-post/", create_post, name="create_post"),
]
