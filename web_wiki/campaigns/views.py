from django.shortcuts import render
from .models import Campaign

def campaigns_list(request):
    campaigns = Campaign.objects.all().order_by('start_date')
    return render(request, 'campaigns_home.html',  #no need to specify template because set in settings
                  { 'campaigns': campaigns}) # return data relative to the Campaign objects


