from django.test import TestCase
from .models import User

class UserTestCase(TestCase):
    def setUp(self):
        User.objects.create(name="test", email="testuser@.com", firstname="test", lastname="user")
        User.objects.create(name="test2", email="testuser2@.com", firstname="test2", lastname="user2")

    def test_Users_have_names(self):
        """Users that have names should return True"""
        test1 = User.objects.get(name="test")
        test2 = User.objects.get(name="test2")
        self.assertEqual(test1.name, 'test')
        self.assertEqual(test2.name, 'test2')

    def test_Users_have_emails_firstnames_lastnames(self):
        test1 = User.objects.get(name="test")
        test2 = User.objects.get(name="test2")
        self.assertEqual(test1.email, 'testuser@.com')
        self.assertEqual(test2.email, 'testuser2@.com')
        self.assertEqual(test1.firstname, 'test')
        self.assertEqual(test2.firstname, 'test2')
        self.assertEqual(test1.lastname, 'user')
        self.assertEqual(test2.lastname, 'user2')

    def test_creating_user_incorrect_email(self):
        with self.assertRaises(ValueError):
            User.objects.create(name="test3", email="testuser3.com", firstname="test3", lastname="user3")

