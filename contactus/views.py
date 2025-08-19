from django.shortcuts import render

def contact_us(request):
    context = {

    }

    return render(request, 'contact_us.html', context)