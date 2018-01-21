from django.shortcuts import render

# Create your views here.

def index(request):
    """defualt index request"""
    return render(request, "cryptoclient/index.html")
