from django.shortcuts import render
from django.views import View
from rest_framework import generics
from .serializers import PostSerializer
from .models import Post


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
