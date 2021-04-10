from django.http import HttpResponse
from django.shortcuts import render
from .models import Chipmunk
def index(request):
    squirrels = Chipmunk.objects.all()[:80]
    context = {
            'squirrels': squirrels,
    }
    return render(request,'squirrel/map.html',{})

# Create your views here.
