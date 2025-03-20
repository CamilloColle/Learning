from django.db import models
from django.utils.text import slugify

class Campaign(models.Model):
    title = models.CharField(max_length=200, unique=True)  # Campaign name
    description = models.TextField(blank=True)  # Optional campaign details
    start_date = models.DateField()  # Campaign start date
    end_date = models.DateField(null=True, blank=True)  # Optional end date
    slug = models.SlugField(blank=True, unique=True)

    def __str__(self):
        return self.title  # Display campaign name in admin panel
    
    def save(self, *args, **kwargs):
        if not self.slug:  # Only generate slug if it's not set
            self.slug = slugify(self.title)
        super().save(*args, **kwargs) 

