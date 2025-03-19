from django.db import models

class Location(models.Model):
    name = models.CharField(max_length=50)
    major_geographical_area = models.CharField(max_length=50)
    description = models.TextField(blank=True)
