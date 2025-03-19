from django.shortcuts import render

def campaigns_list(request):
    return render(request, 'campaigns_home.html') #no need to specify template because set in settings


