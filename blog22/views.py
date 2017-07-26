# -*- coding: utf-8 -*-
"""View File for blog.app."""
from __future__ import unicode_literals
#from blog.models import Post
from django.shortcuts import render
from django.utils import timezone


# Create your views here.
# def post_list(request):
#     """View for Post List Model."""
#     posts = Post.objects.filter(
#         published_date__lte=timezone.now()).order_by('published_date')
#     return render(request, 'blog/post_list.html', {'posts': posts})
