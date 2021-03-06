from django.db import models


class Message(models.Model):
    name = models.CharField(max_length=250)
    email = models.EmailField()
    text = models.TextField()

    def __str__(self):
        return "Message From {name}".format(name=self.name)