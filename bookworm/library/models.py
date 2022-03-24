from django.db import models
from django.contrib.auth.models import User


class Author(models.Model):
    first_name = models.CharField(max_length=200, verbose_name='first name')
    last_name = models.CharField(max_length=200, verbose_name='last name')
    nationality = models.CharField(max_length=200, default=None)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Book(models.Model):
    title = models.CharField(max_length=200, unique=True)
    author = models.ManyToManyField(Author, related_name='books')
    genre = models.CharField(max_length=200)
    user_ratings_id = models.ManyToManyField(User, blank=True, through='Comment')
    rate = models.FloatField(blank=True, null=True)
    summary = models.TextField(blank=True, null=True)
    cover = models.ImageField(upload_to='library/static/covers/', default='static/covers/default-cover.jpeg')
    view_count = models.IntegerField(default=0)
    published_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

