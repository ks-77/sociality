from django.urls import include, path
from rest_framework import routers

from api.views import (CustomUserCreateView, CustomUserDeleteView,
                       CustomUserUpdateView, CustomUserViewSet,
                       PostDetailViewSet, StoryDetailViewSet)

app_name = "api"
router = routers.DefaultRouter()
router.register("customusers", CustomUserViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("api-auth/", include("rest_framework.urls")),
    path("creator/<int:pk>/post/<int:id>/", PostDetailViewSet.as_view()),
    path("creator/<int:pk>/story/<int:id>/", StoryDetailViewSet.as_view()),
    path("customusers/create", CustomUserCreateView.as_view()),
    path("customusers/<int:pk>/update/", CustomUserUpdateView.as_view()),
    path("customusers/<int:pk>/delete/", CustomUserDeleteView.as_view()),
]
