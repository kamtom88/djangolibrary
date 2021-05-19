from django.db import models

from .book import Book
from .publisher import Publisher


class BookEdition(models.Model):

    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    isbn = models.CharField(max_length=17)
    date = models.DateField()

    def __str__(self):
        return "{book}, {publisher}".format(book=self.book, publisher=self.publisher)
