from django.db import models


class Drink(models.Model):
    name = models.CharField(max_length=200, unique=True)
    description = models.CharField(max_length=500, null=True, blank=True)

    def __str__(self):
        return self.name
