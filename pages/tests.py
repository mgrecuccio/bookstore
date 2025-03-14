from django.test import SimpleTestCase
from django.urls import reverse, resolve

from pages.views import HomePageView, AboutPageView


# Create your tests here.
class HomePageTest(SimpleTestCase):
    def setUp(self):
        url = reverse('home')
        self.response = self.client.get(url)


    def test_url_exists_at_correct_location(self):
        self.assertEqual(self.response.status_code, 200)


    def test_homepage_url_name(self):
        self.assertEqual(self.response.status_code, 200)


    def test_homepage_template(self):
        self.assertTemplateUsed(self.response, 'home.html')


    def test_homepage_contains_correct_html(self):
        self.assertContains(self.response, "home page")


    def test_homepage_does_not_contain_incorrect_html(self):
        self.assertNotContains(self.response, 'This should not be present')


    def test_homepage_url_resolves_homepage_view(self):
        view = resolve("/")
        self.assertEqual(view.func.__name__, HomePageView.as_view().__name__)


class AboutPageTest(SimpleTestCase):
    def setUp(self):
        url = reverse('about')
        self.response = self.client.get(url)


    def test_about_page_status_code(self):
        self.assertEqual(self.response.status_code, 200)


    def test_about_page_template(self):
        self.assertTemplateUsed(self.response, 'about.html')


    def test_about_page_contains_correct_html(self):
        self.assertContains(self.response, "About Page")


    def test_about_page_does_not_contain_incorrect_html(self):
        self.assertNotContains(self.response, "This content should not be there")


    def test_about_page_url_resolves_about_page_view(self):
        view = resolve("/about/")
        self.assertEqual(view.func.__name__, AboutPageView.as_view().__name__)