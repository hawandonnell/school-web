from django.db import models
from datetime import datetime

class New(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    pubdate = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title