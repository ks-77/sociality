from django.urls import path

from blog.views import PostDetailView, create_post, create_story, CreationPageView, PostCreationView, StoryCreationView, \
    UserStoriesView

app_name = "blog"


urlpatterns = [
    path("post/<int:pk>/", PostDetailView.as_view(), name="post"),
    path("user/<int:pk>/story/", UserStoriesView.as_view(), name="story"),
    path("generate-story/", create_story, name="generate_story"),
    path("generate-post/", create_post, name="generate_post"),
    path("creation-page/", CreationPageView.as_view(), name="creation_page"),
    path("create-post/", PostCreationView.as_view(), name="create_post"),
    path("create-story/", StoryCreationView.as_view(), name="create_story"),
]
