from django.db import models

from .author import Author
from .book_category import BookCategory


class Book(models.Model):

    tittle = models.CharField(max_length=120)
    # author = models.ForeignKey(Author, on_delete=models.CASCADE)
    authors = models.ManyToManyField(Author)
    sites = models.IntegerField()
    categories = models.ManyToManyField(BookCategory)

    def __str__(self):
        return self.tittle
