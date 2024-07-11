#from django.test import TestCase, Client
from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from .models import Post, Comment
from datetime import date
from django.urls import reverse



class BlogAPITests(APITestCase):
    # Stuff we need for every test...
    def setUp(self):
        # Create a user
        user = User(username='testuser')
        user.set_password('password')
        user.save()
        self.user = user
        self.token = Token.objects.create(user=self.user)
        # self.client = Client()
        # self.client.defaults['HTTP_AUTHORIZATION'] = f'Token {self.token.key}'

        # Create Post
        self.post = Post.objects.create(
            title = 'Test title',
            content = 'Test content',
            author = self.user,
            created_at = date.today(),
            updated_at = date.today(),
        )
        
        self.post = Post.objects.create(
            title = 'Another title',
            content = 'Test content',
            author = self.user,
            created_at = date.today(),
            updated_at = date.today(),
        )

        self.blog_url = reverse("blog_app:posts")
    
    def test_create_post(self):
        self.client.force_authenticate(user=self.user, token=self.token)
        self.assertEqual(2, Post.objects.count())

        data = {
            "title": "Another test title",
            "content": "Another content",
            "created_at": date.today(),
            "updated_at": date.today(),
        }

        response = self.client.post(self.blog_url, data, format="json")
        
        self.assertEqual(3, Post.objects.count())
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    
    def test_get_list_post(self):
        response = Post.objects.all()
        
        self.assertEqual(2, len(response))
        

    def test_get_detail_post(self):
        response = Post.objects.get(pk=1)
        self.assertEqual(response.title, "Test title")

    def test_update_post(self):
        self.client.force_authenticate(user=self.user, token=self.token)
        data = {
            "title": "New title",
            "content": "some nice content",
        }

        response = self.client.put(f'{self.blog_url}1/', data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_post(self):
        self.client.force_authenticate(user=self.user, token=self.token)
        response = self.client.delete(f'{self.blog_url}1/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


class CommentAPITests(APITestCase):
    # Stuff we need for every test...
    def setUp(self):
        # Create a user
        user = User(username='testuser')
        user.set_password('password')
        user.save()
        self.user = user
        self.token = Token.objects.create(user=self.user)
        # self.client = Client()
        # self.client.defaults['HTTP_AUTHORIZATION'] = f'Token {self.token.key}'

        # Create Post
        self.post = Post.objects.create(
            title = 'Test title',
            content = 'Test content',
            author = self.user,
            created_at = date.today(),
            updated_at = date.today(),
        )
        
        self.comment = Comment.objects.create(
            post = self.post,
            content = 'Test comment',
            author = self.user,
            created_at = date.today(),
        )

        self.comment = Comment.objects.create(
            post = self.post,
            content = 'Another Test comment',
            author = self.user,
            created_at = date.today(),
        )

        self.blog_url = reverse("blog_app:comments", kwargs={'post_pk':1})
    
    def test_create_comment(self):
        self.client.force_authenticate(user=self.user, token=self.token)
        self.assertEqual(2, Comment.objects.count())

        data = {
            "content":"Another content"
        }

        response = self.client.post(self.blog_url, data, format="json")
        
        self.assertEqual(3, Comment.objects.count())
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    
    def test_get_list_comment(self):
        response = Comment.objects.all()
        
        self.assertEqual(2, len(response))
        

    def test_get_detail_comment(self):
        response = Comment.objects.get(pk=1)
        self.assertEqual(response.content, "Test comment")

    def test_update_comment(self):
        self.client.force_authenticate(user=self.user, token=self.token)
        data = {
            "content": "new content",
        }

        response = self.client.put(f'{self.blog_url}1/', data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_comment(self):
        self.client.force_authenticate(user=self.user, token=self.token)
        response = self.client.delete(f'{self.blog_url}1/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)