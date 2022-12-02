from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Debate(models.Model):
    debator = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    status = models.BooleanField(default=True)