from django.shortcuts import render

# Create your views here.

def articles(request):
    context = {

    }

    return render(request, 'articles.html', context)