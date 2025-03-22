from django.shortcuts import render
from .models import User

"""
def users_list(request):
    users = User.objects.all().order_by('name')
    return render(request, 'users_list.html', {'users': users})
"""

def register(request):
    return render(request, 'register.html')
    

