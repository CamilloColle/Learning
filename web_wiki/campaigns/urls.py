from django.urls import path
from . import views

app_name = 'campaigns' #specify that these urls are in the app 'campaigns'

urlpatterns = [
    path('', views.campaigns_list, 
         name='list'), #name for the link
    path('new-campaign/', views.campaign_new, 
         name='new-campaign'), #name for the link
    path('<slug:slug>', views.campaign_page, #any hard defined url should go before this otherwise it wil be considered as a slug
         name='page'), 
]
