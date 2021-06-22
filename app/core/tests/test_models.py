from django.test import TestCase
from django.contrib.auth import get_user_model

class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        email = 'cpanchal000@gmail.com'
        password = '123456'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """ test the email for a new user is normalized """
        email = 'cpanchal000@GMAIL.COM'
        user = get_user_model().objects.create_user(
            email=email,
            password='123456'
        )
        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """ error if user with no email """
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, '123456')

    def test_create_new_superuser(self):
        """ test creating new superuser """
        user = get_user_model().objects.create_superuser(
            'admin@gmail.com',
            '123456'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
