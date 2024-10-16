"""Tests for the Django Admin modificatons"""

from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.test import Client


class AdminSiteTests(TestCase):
    """Tests for Django admin"""

    def setUp(self):
        """create user and client"""
        """this is the Django test client that allows us to ake http
        requests"""
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            email='admin@example.com',
            password='test123',
        )
        """force authentication to the user created above"""
        self.client.force_login(self.admin_user)
        self.user = get_user_model().objects.create_user(
            email='user@example.com',
            password='test123',
            name='Test User'
        )

    def test_users_list(self):
        """test users are listed on page"""
        url = reverse('admin:core_user_changelist')
        """makes http get request to the url"""
        res = self.client.get(url)

        """checking that the page contains the name of the user we created
            above"""
        self.assertContains(res, self.user.name)
        """checking that the page containst the email of the user we
        created"""
        self.assertContains(res, self.user.email)

    def test_edit_user_page(self):
        """Test the edit user page works"""
        """do a reverse URL here with diff URL
            should get a url that looks like:
            url = http://localhost:8000/admin/core/user/1/change/
        """
        url = reverse('admin:core_user_change', args=[self.user.id])
        res = self.client.get(url)

        """make sure the page loads successfully """
        self.assertEqual(res.status_code, 200)

    def test_create_user_page(self):
        """test create user page works"""
        url = reverse('admin:core_user_add')
        res = self.client.get(url)

        self.assertEqual(res.status_code, 200)
