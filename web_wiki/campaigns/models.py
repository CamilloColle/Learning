from django.db import models

from django.db import models

class Campaign(models.Model):
    title = models.CharField(max_length=200, unique=True)  # Campaign name
    description = models.TextField(blank=True)  # Optional campaign details
    start_date = models.DateField()  # Campaign start date
    end_date = models.DateField(null=True, blank=True)  # Optional end date

    def __str__(self):
        return self.title  # Display campaign name in admin panel

