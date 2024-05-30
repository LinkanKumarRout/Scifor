from django.shortcuts import render
from .models import *

# Create your views here.
def home(request):
    portfolio = Portfolio.objects.all()
    context = {
        'portfolio':portfolio
    }
    return render(request, 'index.html', context)