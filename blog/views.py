# -*- coding: utf-8 -*-
"""View File for blog.app."""
from __future__ import unicode_literals
from django.shortcuts import render
from django.utils import timezone
from .models import Post


# Create your views here.
# def post_list(request):
#     """View for Post List Model."""
#     posts = Post.objects.filter(
#         published_date__lte=timezone.now()).order_by('published_date')
#     return render(request, 'blog/post_list.html', {'posts': posts})

def home(request):
    return render(request, 'index.html')

def diy_cal(request):
    return render(request, 'blog/diy-cal.html')

def yolo_irc(request):
    return render(request, 'blog/yolo_irc.html')


def blog_post(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    #posts = map(str, Post.objects.filter(published_date__lte=timezone.now().order_by('published_date'))


    return render(request, 'blog/post_list.html', {'posts': posts})
