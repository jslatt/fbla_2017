from __future__ import unicode_literals

from django.db import models
from datetime import date


class employee(models.Model):
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    wage = models.DecimalField(max_digits=4, decimal_places=2, default=13.00)
    hire_date = models.DateField(default=date.today)

    def __str__(self):
            return self.lastName


class generate(models.Model):
    day = models.DateField(default=date.today)
    half = models.TimeField(default=12)