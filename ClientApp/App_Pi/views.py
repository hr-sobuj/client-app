from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'App_Pi/index.html', {})
    