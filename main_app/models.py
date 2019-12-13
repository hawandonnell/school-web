from django.db import models
from django.utils import timezone

class New(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    pubdate = models.DateTimeField(auto_now_add=timezone.localtime(timezone.now()))

    def __str__(self):
        return self.title