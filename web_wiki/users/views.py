from django.shortcuts import render, redirect
from .models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login

"""
def users_list(request):
    users = User.objects.all().order_by('name')
    return render(request, 'users_list.html', {'users': users})
"""

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            login(request, form.save()) #form.save will also return a user value
            return redirect("campaigns:list") #redirect to app 'campaigns', urls with name 'list'
    else: #ie if not submitted via POST method
        form = UserCreationForm() #create empty form
    return render(request, 'register.html', #and return empty form
                  {'form': form})
    
    
def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user()) #fetch user from form if valid
            return redirect('campaigns:list')
    else:
        form = AuthenticationForm()
        
    return render(request, 'login.html', #and return empty form
                  {'form': form})
    

