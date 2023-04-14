"""User tester
"""
from django.contrib.auth import get_user_model
from django.test import TestCase

"""Execute tests for user managment
"""
class UserTests(TestCase):
    """User tester class derived from Testcase

    Args:
        TestCase (obj): Base test case
    """
 
    def test_create_superuser(self):
        """Tests super user creation.
        """
        User = get_user_model()
        admin_user = User.objects.create_superuser(email="super@user.com", password="foo", username="super")
        self.assertEqual(admin_user.email, "super@user.com")
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)
        self.assertEqual(admin_user.username, 'super')


    def test_create_user(self):
        """Tests normal user creation.
        """
        User = get_user_model()
        user = User.objects.create_user(email="normal@user.com", password="foo", username="normal")
        self.assertEqual(user.email, "normal@user.com")
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)
        self.assertEqual(user.username, 'normal')
    
    def test_create_user_profile(self):
        """Tests user profile creation. To be implemented
        """
        pass