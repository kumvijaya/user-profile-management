"""Admin panel tester
"""
from django.test import TestCase, Client
from django.contrib.auth.models import User

class TestAdminPanel(TestCase):
    """Admin panel tester class derived from Testcase

    Args:
        TestCase (obj): Base test case
    """

    def create_user(self):
        """Create test user
        """
        self.username = "test_admin"
        self.password = User.objects.make_random_password()
        user, created = User.objects.get_or_create(username=self.username)
        user.set_password(self.password)
        user.is_staff = True
        user.is_superuser = True
        user.is_active = True
        user.save()
        self.user = user

    def test_spider_admin(self):
        """Tests admin panel urls by creating and viewing the user.
        """
        self.create_user()
        client = Client()
        client.login(username=self.username, password=self.password)
        admin_pages = [
            "/admin/",
            "/admin/auth/",
            "/admin/auth/group/",
            "/admin/auth/group/add/",
            "/admin/auth/user/",
            "/admin/auth/user/add/"
        ]
        for page in admin_pages:
            resp = client.get(page)
            assert resp.status_code == 200
            assert b'<!DOCTYPE html' in resp.content
