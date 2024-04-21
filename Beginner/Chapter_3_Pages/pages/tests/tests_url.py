# Use TestCase with Database. Else, use SimpleTestCase.
from django.test import SimpleTestCase
from django.urls import reverse

# Create your tests here.

class HomepageTests(SimpleTestCase):
    # Get correct path, check urls.py
    def test_home_page_location(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
    # Get correct name, check urls.py
    def test_home_page_name(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
    # Check if template name is correct, check folder.
    def test_home_template_name(self):
        response = self.client.get(reverse("home"))
        self.assertTemplateUsed(response, "home.html")
    # Check if template content is correct.
    def test_home_template_content(self):
        response = self.client.get(reverse("home"))
        self.assertContains(response, "<h1>Homepage</h1>")
    
    
class AboutpageTests(SimpleTestCase):
    # Get correct path, check urls.py
    def test_about_page_location(self):
        response = self.client.get('/about/')
        self.assertEqual(response.status_code, 200)
    # Get correct name, check urls.py
    def test_about_page_name(self):
        response = self.client.get(reverse("about"))
        self.assertEqual(response.status_code, 200)
    # Check if template name is correct, check folder.
    def test_about_template_name(self):
        response = self.client.get(reverse("about"))
        self.assertTemplateUsed(response, "about.html")
    # Check if template content in html file is correct.
    def test_about_template_content(self):
        response = self.client.get(reverse("about"))
        self.assertContains(response, "<h1>About page</h1>")