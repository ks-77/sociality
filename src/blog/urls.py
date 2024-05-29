from django.urls import path

from blog.views import PostDetailView

app_name = "blog"

urlpatterns = [
    path("post/<int:pk>/", PostDetailView.as_view(), name="post"),
]
