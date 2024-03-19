from django.db import models
from datetime import datetime

# Create your models here.

class Input(models.Model):
    Investment = models.CharField(max_length=100)
    PrisPrStk = models.PositiveIntegerField
    Antall = models.PositiveIntegerField
    Created_At = models.DateTimeField(default=datetime.now, blank=True)
    