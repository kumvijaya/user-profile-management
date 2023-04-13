from django.contrib.auth import get_user_model
from django.test import TestCase

"""Execute tests for user managment
"""
class UserTests(TestCase):

    """Tests super user creation.
    """
    def test_create_superuser(self):
        User = get_user_model()
        admin_user = User.objects.create_superuser(email="super@user.com", password="foo", username="super")
        self.assertEqual(admin_user.email, "super@user.com")
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)
        self.assertEqual(admin_user.username, 'super')

    """Tests normal user creation.
    """
    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(email="normal@user.com", password="foo", username="normal")
        self.assertEqual(user.email, "normal@user.com")
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)
        self.assertEqual(user.username, 'normal')
    
    """Tests user profile creation. To be implemented
    """
    def test_create_user_profile(self):
        pass