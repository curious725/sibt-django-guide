from django.test import TestCase
from django.urls import reverse, resolve

from ..views import signup


class SignUpTests(TestCase):

    def test_signup_view(self):
        url = reverse('accounts:signup')
        response = self.client.get(url)
        self.assertTrue(response.status_code, 200)

    def test_signup_url_resolves_signup_view(self):
        view = resolve('/accounts/signup/')
        self.assertTrue(view.func, signup)
