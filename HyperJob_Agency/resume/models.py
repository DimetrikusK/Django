from django.db import models
from django.contrib.auth.models import User


class Resume(models.Model):
    title = models.TextField(max_length=300)
    description = models.TextField(max_length=1540)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.description
