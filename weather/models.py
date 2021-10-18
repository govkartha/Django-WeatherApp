from django.db import models
from django.db.models.fields import CharField


class City(models.Model):
    name = models.CharField(max_length = 100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'cities'