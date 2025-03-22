from django.urls import path
from . import views

app_name = 'users' #specify that these urls are in the app 'campaigns'

urlpatterns = [
    path('register/', views.register, 
         name='register'), 
]