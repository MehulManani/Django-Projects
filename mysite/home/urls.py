from django.urls import path
from .views import *


urlpatterns = [
    path('', home, name='home'),
    path('aboutus',aboutus, name='aboutus'),
    path('contactus', contactus, name='contactus'),
    path('articles',articles, name='articles'),
    path('display',displayrecords, name='displayrecords'),
    path('formdisplay',formdisplay, name='formdisplay'),
    path('register',register, name='register'),
]
