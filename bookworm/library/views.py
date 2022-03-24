from rest_framework import viewsets
from rest_framework.generics import GenericAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import status
from .serializers import AuthorSerializer, BookSerializer, CommentSerializer, RegisterSerializer, UserSerializer
from .models import Author, Book, Comment


class AuthorViewset(viewsets.ModelViewSet):
    permission_class = (IsAuthenticatedOrReadOnly,)
    serializer_class = AuthorSerializer
    queryset = Author.objects.all()
    filterset_fields = ['first_name', 'last_name', 'nationality']


class BookViewset(viewsets.ModelViewSet):
    permission_class = (IsAuthenticatedOrReadOnly,)
    serializer_class = BookSerializer
    queryset = Book.objects.order_by('-rate')
    filterset_fields = ['title', 'genre', 'author', 'rate']


class CommentViewset(viewsets.ModelViewSet):
    permission_class = (IsAuthenticatedOrReadOnly,)
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()
    filterset_fields = ['user', 'book']

    def get_serializer_context(self):
        context = super(CommentViewset, self).get_serializer_context()
        context['user'] = self.request.user
        return context


class Register(GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args,  **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "user": UserSerializer(
                user, context=self.get_serializer_context()
            ).data, "message": "User Created Successfully",
        })


class LogoutView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        try:
            refresh_token = request.data["refresh_token"]
            token = RefreshToken(refresh_token)
            token.blacklist()

            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as exc:
            return Response(status=status.HTTP_400_BAD_REQUEST)
