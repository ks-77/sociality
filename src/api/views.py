from django.contrib.auth import get_user_model

from rest_framework.generics import RetrieveAPIView, CreateAPIView, RetrieveUpdateAPIView, RetrieveDestroyAPIView
from rest_framework.viewsets import ModelViewSet

from api.serializers import CustomUserSerializer, PostSerializer, StorySerializer, CustomUserCreateSerializer

from blog.models import Post, Story


class CustomUserViewSet(ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = CustomUserSerializer


class CustomUserCreateView(CreateAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = CustomUserCreateSerializer


class CustomUserUpdateView(RetrieveUpdateAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = CustomUserSerializer


class CustomUserDeleteView(RetrieveDestroyAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = CustomUserSerializer


class PostDetailViewSet(RetrieveAPIView):
    serializer_class = PostSerializer

    def get_object(self):
        return Post.objects.get(creator__pk=self.kwargs.get('pk'))


class StoryDetailViewSet(RetrieveAPIView):
    serializer_class = StorySerializer

    def get_object(self):
        return Story.objects.get(creator__pk=self.kwargs.get('pk'))
