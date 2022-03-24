from rest_framework.routers import DefaultRouter
from django.urls import path
from .views import *
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


router = DefaultRouter()

router.register(r'authors', AuthorViewset)
router.register(r'books', BookViewset)
router.register(r'comments', CommentViewset)


urlpatterns = router.urls + [
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', Register.as_view()),
    path('logout/', LogoutView.as_view(), name='auth_logout'),

]
