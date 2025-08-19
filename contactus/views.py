from django.shortcuts import render
from . models import *

def contact_us(request):

    context = {

    }

    return render(request, 'contact_us.html', context)

def about_us(request):

    # ----- query ----- # 

    about_us = AboutUs.objects.first()
    
    links = Link.objects.all()

    # ----- filters ----- # 

    telegram = links.get(title='telegram')

    instagram = links.get(title='instagram')

    context = {
        'about_us' : about_us,
        'links' : links,
        'telegram' : telegram,
        'instagram' : instagram,
    }

    return render(request, 'about_us.html', context)