from django.test import TestCase
from ..forms import SignUpForm


class SignUpFormTests(TestCase):
    def test_form_fields(self):
        form = SignUpForm()
        expected_fields = ['username', 'email', 'password1', 'password2']
        actual_fields = list(form.fields)
        self.assertSequenceEqual(
            expected_fields, actual_fields
        )
