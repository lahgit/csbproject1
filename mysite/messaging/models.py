from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.CharField(max_length=200)

class PrivateMessage(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    receiver = models.CharField(max_length=200)
    text = models.CharField(max_length=200)