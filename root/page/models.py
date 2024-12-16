from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from django.conf import settings


class Post(models.Model):
    class Status(models.TextChoices):
        DRAFT ='DF','draft'
        PUBLISHED = 'PB','published'


    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='blog_posts',
    )
    body = models.TextField()
    publish=models.DateTimeField(default=timezone.now)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    
    Status=models.CharField(choices=Status,
                            max_length=10,
                            default=Status.DRAFT
                            )

    class Meta:
        ordering = ['-publish']
        indexes=[
            models.Index(fields=['-publish']),
        ]

    def __str__(self):
        return self.title
