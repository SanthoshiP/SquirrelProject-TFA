from django.shortcuts import render
from django.shortcuts import redirect

from django.http import HttpResponse

from .forms import Form
from squirrel.models import Chipmunk

def list_of_squirrels(request):
    squirrels = Chipmunk.objects.all()
    context = {
            'squirrels': squirrels
            }        
    return render(request, 'squirrel/list_of_squirrels.html', context)

def edit_sightings(request, unique_squirrel_id):
    squirrel = Chipmunk.objects.get(unique_squirrel_id = unique_squirrel_id)

    if request.method == 'POST':
        form = Form(request.POST, instance=squirrel)

        if form.is_valid():
            form.save()
            return redirect('/sightings/')

        else:
            form = Form(instance=squirrel)

        context = {
                'form': form,
        }

        return render(request, 'squirrel/edit_sightings.html', context)

def add_sightings(request):
    
    if request.method == 'POST':
        form = Form(request, POST)

        if form.is_valid():
            form.save()
            return redirect ('/sightings/')

        else:
            form = Form()

            context = {
                    'form': form,
            }
    
            return render(request, 'squirrel/add_sightings.html', context)

# Create your views here.
