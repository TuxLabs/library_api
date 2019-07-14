from django.shortcuts import render
from rest_framework import viewsets
from .serializers import BookSerializer, BookCategorySerializer
from .models import Book, BookCategory

# Create your views here.
class BookViewSet(viewsets.ModelViewSet):
    queryset =  Book.objects.all()
    serializer_class = BookSerializer

class BookCategoryViewSet(viewsets.ModelViewSet):
    queryset = BookCategory.objects.all()
    serializer_class = BookCategorySerializer