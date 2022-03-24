from rest_framework import viewsets
from .serializers import AuthorSerializer, BookSerializer
from .models import Author, Book


class AuthorViewset(viewsets.ModelViewSet):
    serializer_class = AuthorSerializer
    queryset = Author.objects.all()


class BookViewset(viewsets.ModelViewSet):
    serializer_class = BookSerializer
    queryset = Book.objects.order_by('-rate')
