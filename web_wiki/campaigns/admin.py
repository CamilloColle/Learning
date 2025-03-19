from django.contrib import admin
from .models import Campaign

admin.site.register(Campaign)  # Makes Campaign visible in the Django Admin
