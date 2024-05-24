from django.contrib.auth import get_user_model
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase
from django.urls import reverse
from django.utils import timezone
from rest_framework.status import (HTTP_200_OK, HTTP_201_CREATED,
                                   HTTP_401_UNAUTHORIZED, HTTP_403_FORBIDDEN,
                                   HTTP_405_METHOD_NOT_ALLOWED)
from rest_framework.test import APIClient

from accounts.models import CustomUser
from blog.models import Post, Story


class TestApi(TestCase):
    def setUp(self):
        self.client = APIClient()

        self.user = get_user_model()(username="test2342", email="test@example.com", phone_number="+4622658907")
        self.user.set_password("123asdfg345")
        self.user.save()
        self.client.login(username="test2342", password="123asdfg345")

        self.media_file = SimpleUploadedFile("file.mp4", b"file_content", content_type="video/mp4")

        self.post = Post.objects.create(
            creator=self.user,
            media_file=self.media_file,
            description="Test Post",
            location="52.5200,13.4050",
            creation_date=timezone.now(),
        )
        self.story = Story.objects.create(
            creator=self.user, media_file=self.media_file, location="52.5200,13.4050", creation_date=timezone.now()
        )

    def test_user_no_access(self):
        response = self.client.get(reverse("api:schema-swagger"))
        self.assertEqual(response.status_code, HTTP_401_UNAUTHORIZED)

    def test_user_not_allowed(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.get(reverse("api:token_obtain_pair"))
        self.assertEqual(response.status_code, HTTP_405_METHOD_NOT_ALLOWED)

    def test_post_detail(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.get(reverse("api:post_detail", kwargs={"pk": self.user.pk, "id": self.post.id}))
        self.assertEqual(response.status_code, HTTP_200_OK)

    def test_story_detail(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.get(reverse("api:story_detail", kwargs={"pk": self.user.pk, "id": self.story.id}))
        self.assertEqual(response.status_code, HTTP_200_OK)

    def test_create_user(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.post(
            reverse("api:customuser_create"), data={"username": "testtest", "password": "testtesttest"}
        )
        self.assertEqual(response.status_code, HTTP_201_CREATED)

    def test_update_custom_user(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.put(
            reverse("api:customuser_update", kwargs={"pk": self.user.pk}), data={"username": "updateduser"}
        )
        self.assertEqual(response.status_code, HTTP_200_OK)
