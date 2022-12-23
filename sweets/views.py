from django.shortcuts import render
from .models import Sweets

def index(request):
    sweets = Sweets.objects.all()
    return render (request, 'home.html', {'sweets': sweets})
