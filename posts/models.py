from django.db import models


class Post(models.Model):
    title=models.CharField(max_length=255)
    slug=models.SlugField(max_length=255)
    description=models.TextField(max_length=255)
