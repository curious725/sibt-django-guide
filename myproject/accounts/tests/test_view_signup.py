from django.test import TestCase
from django.urls import reverse, resolve
from django.contrib.auth.forms import UserCreationForm

from ..views import signup


class SignUpTests(TestCase):
    def setUp(self):
        url = reverse('accounts:signup')
        self.response = self.client.get(url)

    def test_signup_view(self):
        self.assertTrue(self.response.status_code, 200)

    def test_signup_url_resolves_signup_view(self):
        view = resolve('/accounts/signup/')
        self.assertTrue(view.func, signup)

    def test_signup_template_includes_csrf(self):
        self.assertContains(self.response, 'csrfmiddlewaretoken')

    def test_signup_template_contains_form(self):
        form = self.response.context.get('form')
        self.assertIsInstance(
            form, UserCreationForm
        )
