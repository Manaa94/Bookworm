from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()

router.register(r'authors', AuthorViewset)
router.register(r'books', BookViewset)
router.register(r'comments', CommentViewset)



urlpatterns = router.urls