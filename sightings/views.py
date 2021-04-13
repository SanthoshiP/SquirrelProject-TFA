from django.shortcuts import render

from squirrel.models import Chipmunk

def list_of_squirrels(request):
    squirrels = Chipmunk.objects.all()
    context = {
            'squirrels': squirrels
            }        
    return render(request, 'squirrel/list_of_squirrels.html', context)

# Create your views here.
