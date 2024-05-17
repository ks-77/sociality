from django.contrib.auth import get_user_model
from django.core.files.storage import default_storage
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import Client, TestCase
from django.utils import timezone

from accounts.models import UserProfile
from posts.models import Post


class TestPostModel(TestCase):
    def setUp(self):
        self.client = Client()
        User = get_user_model()

        self.user1 = User(username="user1", email="user1@gmail.com")
        self.user1.set_password("useruser1")
        self.user1.save()

        self.user_profile1 = UserProfile(user=self.user1)
        self.user_profile1.save()

    def tearDown(self):
        default_storage.delete("posts/testphoto.jpg")
        default_storage.delete("posts/testvideo.mp4")
        default_storage.delete("posts/testfile.jpg")

    def test_create_photo_post(self):
        photo_file = SimpleUploadedFile("testphoto.jpg", b"photo_content", content_type="image/jpeg")
        post = Post(
            creator=self.user_profile1,
            media_file=photo_file,
            description="A test photo post",
            location="36.5672,-5.6876",
            creation_date=timezone.now(),
        )
        post.save()

        self.assertEqual(Post.objects.count(), 1)
        self.assertEqual(post.creator, self.user_profile1)
        self.assertEqual(post.description, "A test photo post")
        self.assertEqual(post.location, "36.5672,-5.6876")
        self.assertIn("testphoto.jpg", post.media_file.name)

    def test_create_video_post(self):
        video_file = SimpleUploadedFile("testvideo.mp4", b"video_content", content_type="video/mp4")
        post = Post(
            creator=self.user_profile1,
            media_file=video_file,
            description="A test video post",
            location="36.5672,-5.6876",
            creation_date=timezone.now(),
        )
        post.save()

        self.assertEqual(Post.objects.count(), 1)
        self.assertEqual(post.creator, self.user_profile1)
        self.assertEqual(post.description, "A test video post")
        self.assertEqual(post.location, "36.5672,-5.6876")
        self.assertIn("testvideo.mp4", post.media_file.name)

    def test_delete_post(self):
        media_file = SimpleUploadedFile("testfile.jpg", b"file_content", content_type="image/jpeg")
        post = Post(
            creator=self.user_profile1,
            media_file=media_file,
            description="A test post",
            location="36.5672,-5.6876",
            creation_date=timezone.now(),
        )
        post.save()

        post.delete()

        self.assertEqual(Post.objects.count(), 0)
