from django.urls import path
from . views import *

urlpatterns = [
    path('contactus', contact_us, name='contactus'),
]
