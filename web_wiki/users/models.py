from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(blank=True)
    join_date = models.DateField()

    def __str__(self):
        return self.name