from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse, resolve
from dictionary.api.viewsets import AttemptsViewSet
from django.contrib.auth.views import LoginView

class TestAuth(TestCase):

    def setUp(self):
        self.client = Client()
        self.login_url = reverse('login')
        self.credentials = {
            'username': 'testuser',
            'password': 'secret'}
        User.objects.create_user(**self.credentials)
        self.credentials['next'] = reverse('attempts-list')

    def test_login_successful(self):
        response = self.client.post(self.login_url, self.credentials, follow=True)
        self.assertEqual(response.status_code, 200)
        # redirection to attempts page before the login
        self.assertEqual(resolve(self.credentials['next']).func.cls, AttemptsViewSet)

    def test_login_failed(self):
        self.client.logout()
        self.credentials['username'] = 'wrong_secret'
        response = self.client.post(self.login_url, self.credentials)
        self.assertEqual(response.status_code, 200)
        self.assertFalse(response.context['user'].is_active)
