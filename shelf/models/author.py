from django.db import models


class Author(models.Model):

    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=50)

    def __str__(self):
        return "{first_name} {last_name}".format(first_name=self.first_name, last_name=self.last_name)

