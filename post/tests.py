from django.test import TestCase
from django.contrib.auth.models import User
from .models import Post


class BlogTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        # Create a user
        testuser1 = User.objects.create_user(username='test1', password='abc123')
        testuser1.save()

        # Create a blog post
        test_post = Post.objects.create(author=testuser1, title='Blog title', body='Content...')
        test_post.save()

    def test_blog_content(self):
        post = Post.objects.get(id=1)
        author = f'{post.author}'
        title = f'{post.title}'
        body = f'{post.body}'
        self.assertEqual(author, 'test1')
        self.assertEqual(title, 'Blog title')
        self.assertEqual(body, 'Content...')
