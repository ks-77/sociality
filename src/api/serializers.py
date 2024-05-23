from django.contrib.auth import get_user_model
from rest_framework.serializers import ModelSerializer

from blog.models import Post


class CustomUserSerializer(ModelSerializer):
    class Meta:
        model = get_user_model()
        exclude = ["password"]


class CustomUserCreateSerializer(ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ["username", "email", "phone_number", "password"]


class PostSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = ["id", "media_file", "description", "location"]


class StorySerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = ["id", "media_file", "location"]
