# hello_azure/models.py
from django.db import models

class YourModel(models.Model):
    # Your model fields here
    name = models.CharField(max_length=255)
