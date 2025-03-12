from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse, resolve

from .forms import CustomUserCreationForm
from .views import SignupPageView


# Create your tests here.
class CustomUserTests(TestCase):
    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(
            username="testUser",
            email="test@email.com",
            password="testPass123",
        )

        self.assertEqual(user.username, "testUser")
        self.assertEqual(user.email, "test@email.com")
        self.assertFalse(user.is_superuser)
        self.assertFalse(user.is_staff)
        self.assertTrue(user.is_active)


    def test_create_superuser(self):
        User = get_user_model()
        user = User.objects.create_superuser(
            email="admin@email.com",
            username="testSuperUser",
            password="testPass123",
        )

        self.assertEqual(user.username, "testSuperUser")
        self.assertEqual(user.email, "admin@email.com")
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
        self.assertTrue(user.is_active)


class SignUpPageViewTest(TestCase):
    def setUp(self):
        url = reverse('signup')
        self.response = self.client.get(url)


    def test_signup_template(self):
        self.assertEqual(self.response.status_code, 200)
        self.assertTemplateUsed(self.response, "registration/signup.html")
        self.assertContains(self.response, "Sign Up")


    def test_signup_view(self):
        view = resolve('/accounts/signup/')
        self.assertEqual(view.func.__name__, SignupPageView.as_view().__name__)


    def test_signup_form(self):
        form = self.response.context.get('form')
        self.assertIsInstance(form, CustomUserCreationForm)