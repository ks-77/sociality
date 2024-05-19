from django.contrib.auth import get_user_model
from django.test import Client, TestCase
from subscriptions.models import Subscription

from accounts.models import UserProfile


class TestSubscriptionModel(TestCase):
    def setUp(self):
        self.client = Client()
        User = get_user_model()

        self.user1 = User(username="user1", email="user1@gmail.com")
        self.user1.set_password("useruser1")
        self.user1.save()
        self.user2 = User(username="user2", email="user2@gmail.com")
        self.user2.set_password("useruser2")
        self.user2.save()

        self.user_profile1 = UserProfile(user=self.user1)
        self.user_profile1.save()
        self.user_profile2 = UserProfile(user=self.user2)
        self.user_profile2.save()

    def test_create_subscription(self):
        subscription = Subscription(subscriber=self.user_profile1, author=self.user_profile2)
        subscription.save()

        self.assertEqual(Subscription.objects.count(), 1)
        self.assertEqual(subscription.subscriber, self.user_profile1)
        self.assertEqual(subscription.author, self.user_profile2)

    def test_delete_subscription(self):
        subscription = Subscription(subscriber=self.user_profile1, author=self.user_profile2)
        subscription.save()

        subscription.delete()

        self.assertEqual(Subscription.objects.count(), 0)
