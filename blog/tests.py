from django.test import TestCase, client
from django.contrib.auth import get_user_model
from django.urls import reverse

from .models import Post

class BlogTest(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username = 'testuser',
            email='testuser@email.com',
            password='secret'
        )

        self.post = Post.objects.create(
            title = 'Test case one',
            body = 'This is the fist test django case for blog.',
            author = self.user,
        )
    
    def test_string_representation(self):
        post = Post(title='A simple title')
        self.assertEqual(str(post), post.title)