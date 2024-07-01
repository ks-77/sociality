import random

from faker import Faker

from accounts.models import CustomUser
from blog.models import Post
from interactions.models import Comment, Like, Subscription

fake = Faker()


def generate_comment():
    post = random.choice(Post.objects.all())
    user = random.choice(CustomUser.objects.all())
    comment = Comment.objects.create(
        post=post,
        user=user,
        content=fake.text(max_nb_chars=150),
    )
    return comment


def generate_like():
    post = random.choice(Post.objects.all())
    user = random.choice(CustomUser.objects.all())
    like, created = Like.objects.get_or_create(
        post=post,
        user=user,
    )
    return like


def generate_subscription():
    subscriber = random.choice(CustomUser.objects.all())
    author = random.choice(CustomUser.objects.all())
    if subscriber != author:
        subscription, created = Subscription.objects.get_or_create(
            subscriber=subscriber,
            author=author,
        )
        return subscription
