from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

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


class SignupPageTest(TestCase):
    username = "new-user"
    email = "new-user@email.com"

    def setUp(self):
        url = reverse("account_signup")
        self.response = self.client.get(url)

    def test_signup_template(self):
        self.assertEqual(self.response.status_code, 200)
        self.assertTemplateUsed(self.response, "account/signup.html")
        self.assertContains(self.response, "Sign Up")

    def test_signup_form(self):
        new_user = get_user_model().objects.create_user(
            self.username,
            self.email,
        )
        self.assertEqual(get_user_model().objects.count(), 1)
        self.assertEqual(get_user_model().objects.all()[0].username, self.username)
        self.assertEqual(get_user_model().objects.all()[0].email, self.email)

