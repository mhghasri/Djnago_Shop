from django.shortcuts import render
from django.http import HttpResponse
from . forms import *

# Create your views here.

def signup(request):

    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():    
            form.save()
            return HttpResponse("this is done! welcome dear user.")
            
        else:
            return HttpResponse("Please try again invalid input")
        
    form = UserForm()

    context = {
        "form" : form
    }

    return render(request, 'signup.html', context)