

# Create your models here.
# models.py
from django.db import models

class Dream(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    interpretation = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title
