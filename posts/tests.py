from django.test import TestCase
from django.urls import reverse
from .models import Post

class PostModelTest(TestCase):

    def setUp(self):
        Post.objects.create(text='Testing post')

    def test_post_text(self):
        post = Post.objects.get(id=1)
        expected = f'{post.text}'
        print(expected)
        self.assertCountEqual(expected, 'Testing post')

class PostViewTest(TestCase):

    def setUp(self):
        Post.objects.create(text='Second testing post')

    def test_view_url(self):
        resp = self.client.get('/posts/')
        self.assertEqual(resp.status_code, 200)
    
    def test_view_url_by_name(self):
        resp = self.client.get(reverse('home'))
        self.assertEqual(resp.status_code, 200)
    
    def test_view_template(self):
        resp = self.client.get(reverse('posts'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'posts.html')
