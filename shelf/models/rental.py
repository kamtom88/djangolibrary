from django.db import models
from django.contrib.auth.models import User
from .book_item import BookItem
from django.utils.timezone import now


class Rental(models.Model):
    who = models.ForeignKey(User, on_delete=models.CASCADE)
    what = models.ForeignKey(BookItem, on_delete=models.CASCADE)
    when = models.DateTimeField(default=now)
    returned = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return "{who}, {what}, {when}".format(who=self.who, what = self.what, when=self.when)
