from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from . forms import *

# Create your views here.

def signup(request):

    alert = None

    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():    
            form.save()
            alert = True
            
        else:
            alert = False
        
    form = UserForm()

    context = {
        "form" : form,
        "alert" : alert
    }

    return render(request, 'signup.html', context)