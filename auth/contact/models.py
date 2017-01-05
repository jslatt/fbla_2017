from __future__ import unicode_literals

from django.db import models
from datetime import datetime


class contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    message = models.TextField(max_length=1000)
    subject = models.CharField(max_length=140, default="Customer Message")
    subDate = models.DateTimeField(default=datetime.now, blank=True)
    read = models.BooleanField(default=True, blank=True)

    def __str__(self):
        return self.name
