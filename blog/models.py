# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone


# Create your models here.
class Post(models.Model):
    """Currently we are running a Blog models."""

    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        """We are setting date and saving to db."""
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        """This is where the magic happens, our title is returned,

        we will be returning the date, and published date also.
        """

        return self.title
