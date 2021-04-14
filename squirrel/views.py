from django.http import HttpResponse
from django.shortcuts import render
from .models import Chipmunk

def map(request):
    squirrels= list(Chipmunk.objects.all())[:80]
    context = {
            'squirrels': squirrels,
    }
    return render(request,'squirrel/map.html', context)

def home(request):
    return render(request,'squirrel/index.html')

# Create your views here.
