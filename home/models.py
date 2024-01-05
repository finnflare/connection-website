from django.db import models


class Contacts(models.Model):
    email = models.EmailField(max_length=254)
    time = models.DateTimeField("date contacted")
    message = models.TextField()