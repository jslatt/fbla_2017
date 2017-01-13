from __future__ import unicode_literals
from django.contrib.auth import get_user_model, settings
from django.db import models
from datetime import datetime


class reserve(models.Model):
    package = models.CharField(max_length=100)
    comments = models.TextField(max_length=1000)
    time = models.DateField(default=datetime.now, blank=True)
    email = models.CharField(default="Bob@bob.com", max_length=100)
    approved = models.BooleanField(default=False)

    def __unicode__(self):
        return self.comments
