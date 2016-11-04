from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Signupuser(models.Model):
    username = models.TextField(default=True)
    password = models.TextField(default=True)
