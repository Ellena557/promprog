from django.conf import settings
from django.db import models


class Post(models.Model):
    
    title = models.CharField(max_length=300)
    text = models.TextField(max_length=5000)

    def publish(self):
        self.save()

    def __str__(self):
        return self.title
