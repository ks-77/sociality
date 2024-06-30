from django.urls import path

from core.views import ComingSoonView

app_name = "core"

urlpatterns = [
    path("comingsoon/", ComingSoonView.as_view(), name="comingsoon"),
]
