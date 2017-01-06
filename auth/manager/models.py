from __future__ import unicode_literals
from django.db import models
from datetime import datetime


class employee(models.Model):
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    wage = models.DecimalField(max_digits=4, decimal_places=2, default=13.00)

    def __str__(self):
            return self.lastName

