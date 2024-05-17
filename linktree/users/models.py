# linktree/models.py
from django.db import models

class UserProfile(models.Model):
    name = models.CharField(max_length=100, default='')
    lastname = models.CharField(max_length=100, default='')
    birthday = models.DateField(null=True)
    phone_number = models.CharField(max_length=20, default='')
    email = models.EmailField(default='')
    short_description = models.TextField(default='')
    profile_picture = models.URLField(default='')