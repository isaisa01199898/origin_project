from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    favorite_category = models.CharField(max_length=100, blank=True)


class Diary(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    diary_date = models.DateField()

    def __str__(self):
        return self.title
