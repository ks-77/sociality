from django.urls import include, path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions, routers
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView)

from api.views import (CustomUserCreateView, CustomUserDeleteView,
                       CustomUserUpdateView, CustomUserViewSet,
                       PostDetailViewSet, StoryDetailViewSet)

app_name = "api"
router = routers.DefaultRouter()
router.register("customusers", CustomUserViewSet)


schema_view = get_schema_view(
    openapi.Info(
        title="Snippets API",
        default_version="v1",
        description="Test description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.IsAuthenticated,),
)

urlpatterns = [
    path("docs/", schema_view.with_ui("swagger", cache_timeout=0), name="schema-swagger"),
    path("", include(router.urls)),
    path("auth/", include("djoser.urls.jwt")),
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("creator/<int:pk>/post/<int:id>/", PostDetailViewSet.as_view(), name="post_detail"),
    path("creator/<int:pk>/story/<int:id>/", StoryDetailViewSet.as_view(), name="story_detail"),
    path("customusers/create", CustomUserCreateView.as_view(), name="customuser_create"),
    path("customusers/<int:pk>/update/", CustomUserUpdateView.as_view(), name="customuser_update"),
    path("customusers/<int:pk>/delete/", CustomUserDeleteView.as_view()),
]
