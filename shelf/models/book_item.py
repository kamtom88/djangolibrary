from django.db import models

from .book_edition import BookEdition
from .book import Book
COVER_TTYPES = (
    ('soft', 'Soft'),
    ('hard', 'Hard')
)


class BookItem(models.Model):

    edition = models.ForeignKey(BookEdition, on_delete=models.CASCADE)
    catalogue_number = models.CharField(max_length=30)
    cover_type = models.CharField(max_length=4, choices=COVER_TTYPES)

    def __str__(self):
        return "{edition}, {cover}".format(edition=self.edition, cover=self.cover_type)
