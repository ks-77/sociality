from django.contrib.auth import get_user_model
from django.test import Client, TestCase


class TestAuthCustomUser(TestCase):
    def setUp(self):
        self.client = Client()

        self.user = get_user_model()(email="user@gmail.com")
        self.user.username = "user"
        self.user.set_password("useruser")
        self.user.save()

        self.manager = get_user_model()(email="manager@gmail.com")
        self.manager.username = "manager"
        self.manager.set_password("manager")
        self.manager.is_staff = True
        self.manager.save()

    def test_user_wrong_email(self):
        user_login = self.client.login(email="wrong@gmail.com", password="useruser")
        self.assertFalse(user_login)

    def test_user_wrong_username(self):
        user_login = self.client.login(username="wrong_user", password="useruser")
        self.assertFalse(user_login)

    def test_user_wrong_password(self):
        user_login = self.client.login(username="user", password="wronguseruser")
        self.assertFalse(user_login)

    def test_user_correct_info(self):
        user_login = self.client.login(username="user", password="useruser")
        self.assertTrue(user_login)
        self.assertEqual(user_login, True)
