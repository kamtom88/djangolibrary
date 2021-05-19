from django.db import models


class Publisher(models.Model):

    name = models.CharField(max_length=70)

    def __str__(self):
        return self.name
