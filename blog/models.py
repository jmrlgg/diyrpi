# -*- coding: utf-8 -*-
"""Models CONFIGURATION."""

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils import timezone
from taggit.managers import TaggableManager


# Create your models here.
class Post(models.Model):
    """Post Model."""

    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
        default=timezone.now)
    published_date = models.DateTimeField(
        blank=True, null=True)
    tags = TaggableManager()

    def publish(self):
        """We are setting date and saving to db."""
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        """Post Model Return.

        Where the magic happens our title is returned
        we will be returning the date, and published date also.
        """
        return self.title


class TaggableManager():
    verbose_name = "Tags"
    help_text = "A comma-separated list of tags."
    through = None
    blank = False

    # Post extra OPTIONS
    # class Meta:
    #     """Post Extra Features."""
    #
    #     order = ['published_date']
