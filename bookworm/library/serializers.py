from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Author, Book, Comment


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ('id', 'first_name', 'last_name', 'nationality')
        read_only_fields = ('id')


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('id', 'title', 'author', 'genre', 'rate',
                  'summary', 'cover', 'view_count', 'published_at')
        read_only_fields = ('id', 'rate', 'view_count')


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id', 'user', 'book', 'rating', 'text')
        read_only_fields = ('id', 'user')

    def create(self, validated_data):
        user = self.context['user']
        validated_data["user"] = user
        instance = super().create(validated_data)
        return instance



class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','username','password','first_name', 'last_name')
        extra_kwargs = {
            'password':{'write_only': True},
        }

    def create(self, validated_data):
        user = User.objects.create_user(
            validated_data['username'],     
            password = validated_data['password'],
            first_name=validated_data['first_name'],  
            last_name=validated_data['last_name']
            )
        return user


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

