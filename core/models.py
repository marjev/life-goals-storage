from django.db import models


class Game(models.Model):
    codename = models.CharField(max_length=25)
    release_date = models.DateField()

    def __str__(self):
        return f"Pokemon {self.codename}"
