from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

class Tweet(models.Model):
    message = models.CharField(max_length=50, null=False)
    date = models.DateTimeField(auto_now_add=datetime.now)
    name =models.CharField(max_length=50, null=False)

