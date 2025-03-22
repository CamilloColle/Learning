from django.shortcuts import render, redirect
from .models import User
from django.contrib.auth.forms import UserCreationForm

"""
def users_list(request):
    users = User.objects.all().order_by('name')
    return render(request, 'users_list.html', {'users': users})
"""

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("campaigns:list") #redirect to app 'campaigns', urls with name 'list'
    else: #ie if not submitted via POST method
        form = UserCreationForm() #create empty form
    return render(request, 'register.html', #and return empty form
                  {'form': form})
    

