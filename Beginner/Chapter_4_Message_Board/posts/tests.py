from django.test import TestCase
from django.urls import reverse
from .models import Post
# Create your tests here.

'''
class HomepageTests(TestCase):
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
    
# Creates a test post and verify that it sees it on the page. 
class PostTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.post = Post.objects.create(text="This is a test!")
    
    def test_model_content(self):
        self.assertEqual(self.post.text, "This is a test!")
    
    # Check if template content is correct (Should find post from PostTests).
    def test_home_template_content(self):
        response = self.client.get(reverse("home"))
        self.assertContains(response, "This is a test!")
'''

# Simplify both classes
class PostTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.post = Post.objects.create(text="This is a test!")
    
    def test_model_content(self):
        self.assertEqual(self.post.text, "This is a test!")

    def test_url_exists_at_correct_location(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
    
    def test_homepage(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "home.html")
        self.assertContains(response, "This is a test!")
