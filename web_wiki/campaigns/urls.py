from django.urls import path
from . import views

app_name = 'campaigns' #specify that these urls are in the app 'campaigns'

urlpatterns = [
    path('', views.campaigns_list, 
         name='list'), #name for the link
    path('<slug:slug>', views.campaign_page, 
         name='page'), 
]
