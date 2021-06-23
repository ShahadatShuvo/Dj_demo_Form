from django.db import models

# Create your models here.


class Author(models.Model):
    name = models.CharField(max_length=30)
    age = models.PositiveIntegerField()
    city = models.CharField(max_length=20)

    def __str__(self):
        return str(self.name)