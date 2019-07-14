from django.db import models
from common.models import BaseModelGeneric

# Create your models here.

class BookCategory(BaseModelGeneric):
    name = models.CharField(max_length=10, blank = True)

    class Meta:
        verbose_name = "BookCategory"
        verbose_name_plural = "BookCategories"

class Book(BaseModelGeneric):
    code = models.CharField(max_length=10, blank = True)
    category = models.ForeignKey(BookCategory,on_delete=models.CASCADE, blank = True, null = True)
    title = models.CharField(max_length=250, blank = True)
    author = models.CharField(max_length=250, blank = True)
    published_by = models.CharField(max_length=250, blank = True)
    
    class Meta:
        verbose_name = "Book"
        verbose_name_plural = "Books"

