import tempfile

from django.core.files.uploadedfile import SimpleUploadedFile
from django.utils import timezone

from accounts.models import CustomUser
from blog.models import Post, Story


def sample_post(creator=None, **params):

    if not creator:
        creator = CustomUser.objects.create_user(username="testuser", password="password")

    temp_file = tempfile.NamedTemporaryFile(delete=False)
    temp_file.write(b"Test file content")
    temp_file.seek(0)
    media_file = SimpleUploadedFile(name="testfile.jpg", content=temp_file.read(), content_type="image/jpeg")

    default = {
        "media_file": media_file,
        "description": "Some description",
        "location": None,
        "creation_date": timezone.now(),
    }
    default.update(params)
    return Post.objects.create(creator=creator, **default)


def sample_story(creator=None, **params):

    if not creator:
        creator = CustomUser.objects.create_user(username="testuser", password="password")

    temp_file = tempfile.NamedTemporaryFile(delete=False)
    temp_file.write(b"Test file content")
    temp_file.seek(0)
    media_file = SimpleUploadedFile(name="testfile.jpg", content=temp_file.read(), content_type="image/jpeg")

    default = {
        "media_file": media_file,
        "location": None,
        "creation_date": timezone.now(),
    }
    default.update(params)
    return Story.objects.create(creator=creator, **default)
