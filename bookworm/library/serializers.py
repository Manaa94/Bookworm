from rest_framework import serializers
from .models import Author, Book



class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ('id', 'first_name', 'last_name', 'nationality')
        read_only_field = ('id')


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('id', 'title', 'author', 'genre', 'rate', 'summary', 'cover', 'view_count', 'published_at')
        read_only_field = ('id', 'rate', 'view_count')