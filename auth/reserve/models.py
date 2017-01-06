from __future__ import unicode_literals

from django.db import models
from datetime import datetime


class reserve(models.Model):
    package = models.CharField(max_length=100)
    price = models.IntegerField(default=50)
    comments = models.TextField(max_length=1000)
    time = models.DateTimeField(default=datetime.now, blank=True)
