from django.db import models

class UserMessage(models.Model):
    message = models.TextField()
