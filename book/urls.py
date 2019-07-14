from django.conf.urls import url, include
from rest_framework import routers
from .views import BookCategoryViewSet, BookViewSet

router = routers.DefaultRouter()
router.register(r'book', BookViewSet, 'book')
router.register(r'category', BookCategoryViewSet, 'category')

urlpatterns = [
    url(r'', include(router.urls)),
]
