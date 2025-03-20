from django.shortcuts import render
from .models import Campaign
#from django.http import HttpResponse

def campaigns_list(request):
    campaigns = Campaign.objects.all().order_by('start_date')
    return render(request, 'campaigns_home.html',  #no need to specify template because set in settings
                  { 'campaigns': campaigns}) # return data relative to the Campaign objects


def campaign_page(request, slug):
    campaign = Campaign.objects.get(slug=slug)
    return render(request, 'campaign_page.html',  #render specific page
                  { 'campaign': campaign}) # return data relative to the Campaign objects


