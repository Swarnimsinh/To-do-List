from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_completed = models.BooleanField(default=False)