from django.contrib.auth.models import Permission
from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model

from .models import Book, Review

class BookTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.create(
            username="review-user",
            email="review-user@email.com",
            password="testPass123"
        )

        cls.special_permission = Permission.objects.get(codename="special_status")

        cls.book = Book.objects.create(
            title="Harry Potter",
            author="JK Rowling",
            price="25.00",
        )

        cls.review = Review.objects.create(
            book=cls.book,
            author=cls.user,
            review="An excellent review",
        )

    def test_book_list_view_for_logged_in_user(self): # new
        self.client.force_login(self.user)
        response = self.client.get(reverse("book_list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Harry Potter")
        self.assertTemplateUsed(response, "books/book_list.html")

    def test_book_listing(self):
        self.assertEqual(f"{self.book.title}", "Harry Potter")
        self.assertEqual(f"{self.book.author}", "JK Rowling")
        self.assertEqual(f"{self.book.price}", "25.00")

    def test_book_list_view_for_logged_out_user(self):  # new
        self.client.logout()
        response = self.client.get(reverse("book_list"))
        self.assertEqual(response.status_code, 302)  # new
        self.assertRedirects(
            response, "%s?next=/books/" % (reverse("account_login")))
        response = self.client.get(
            "%s?next=/books/" % (reverse("account_login")))
        self.assertContains(response, "Log In")