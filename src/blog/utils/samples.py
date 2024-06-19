import random

import requests
from django.core.files.base import ContentFile
from faker import Faker

from accounts.models import CustomUser
from blog.models import Post, Story

fake = Faker()


def generate_post():
    user = random.choice(CustomUser.objects.all())

    response = requests.get("https://picsum.photos/600/800", stream=True)
    response.raise_for_status()
    image_content = ContentFile(response.content)
    image_name = f"{fake.word()}.jpg"

    post = Post(
        creator=user,
        description=fake.text(max_nb_chars=150),
        location=fake.location_on_land(),
        media_file=image_content,
    )
    post.media_file.save(image_name, image_content, save=True)
    post.save()
    return post


def generate_story():
    user = random.choice(CustomUser.objects.all())

    response = requests.get("https://picsum.photos/600/800", stream=True)
    response.raise_for_status()
    image_content = ContentFile(response.content)
    image_name = f"{fake.word()}.jpg"

    story = Story(
        creator=user,
        location=fake.location_on_land(),
        media_file=image_content,
        expire_date=fake.date_time_between(start_date="now", end_date="+1d"),
    )
    story.media_file.save(image_name, image_content, save=True)
    story.save()
    return story
