from django.test import TestCase
from django.contrib.auth.models import User

class UserTestCase(TestCase):
    def setUp(self):
        User.objects.create_user(username="test", email="testuser@.com", first_name="test", last_name="user")
        User.objects.create_user(username="test2", email="testuser2@.com", first_name="test2", last_name="user2")

    def test_Users_have_names(self):
        """Users that have names should return True"""
        test1 = User.objects.get(username="test")
        test2 = User.objects.get(username="test2")
        self.assertEqual(test1.username, 'test')
        self.assertEqual(test2.username, 'test2')

    def test_Users_have_emails_firstnames_lastnames(self):
        test1 = User.objects.get(username="test")
        test2 = User.objects.get(username="test2")
        self.assertEqual(test1.email, 'testuser@.com')
        self.assertEqual(test2.email, 'testuser2@.com')
        self.assertEqual(test1.first_name, 'test')
        self.assertEqual(test2.first_name, 'test2')
        self.assertEqual(test1.last_name, 'user')
        self.assertEqual(test2.last_name, 'user2')

from django.contrib.auth.models import User
from django.urls import reverse

class LoginViewTestCase(TestCase):
    def setUp(self):
        self.username = 'testuser'
        self.password = 'testpassword'
        self.user = User.objects.create_user(username=self.username, password=self.password)

    def test_login_view_with_valid_credentials(self):
        response = self.client.post(reverse('login'), {'username': self.username, 'password': self.password})
        self.assertEqual(response.status_code, 200)  

        self.assertTrue(response.wsgi_request.user.is_authenticated)

    def test_login_view_with_invalid_credentials(self):
        response = self.client.post(reverse('login'), {'username': self.username, 'password': 'wrongpassword'})
        self.assertEqual(response.status_code, 401) 

        self.assertFalse(response.wsgi_request.user.is_authenticated)

    def tearDown(self):
        self.user.delete()

