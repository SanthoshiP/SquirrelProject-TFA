from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404

from django.http import HttpResponse

from sightings.forms import Form

from squirrel.models import Chipmunk

from django.views.generic.edit import CreateView, DeleteView

from django.db.models import Count

def list_of_squirrels(request):
    squirrels = Chipmunk.objects.all()
    context = {
            'squirrels': squirrels
            }        
    return render(request, 'squirrel/list_of_squirrels.html', context)

from squirrel.models import Chipmunk

def edit_sightings(request, unique_squirrel_id):
    squirrels = get_object_or_404(Chipmunk, unique_squirrel_id = unique_squirrel_id)

    if request.method == 'POST':
        form = Form(request.POST, instance=squirrels)

        if form.is_valid():
            form.save()
            return redirect('/sightings/')
    else:
        form = Form(instance=squirrels)

    context = {
            'form': form
        }
    return render(request, 'squirrel/edit_sightings.html', context)

from squirrel.models import Chipmunk

def add_sightings(request):
    
    if request.method == 'POST':
        form = Form(request.POST)

        if form.is_valid():
            form.save()
            return redirect ('/sightings/')

    else:
        form = Form()

    context = {
            'form': form
    }
    
    return render(request, 'squirrel/add_sightings.html', context)

from squirrel.models import Chipmunk

def statistics(request):
    number_of_squirrels = Chipmunk.objects.all().count()
    chasing_yes = Chipmunk.objects.filter(chasing=True).count()
    climbing_yes = Chipmunk.objects.filter(climbing=True).count()
    foraging_yes=Chipmunk.objects.filter(foraging=True).count()
    eating_yes = Chipmunk.objects.filter(eating=True).count()
    context = {
            'number_of_squirrels':number_of_squirrels,
            'chasing_yes':chasing_yes,
            'climbing_yes':climbing_yes,
            'foraging_yes':foraging_yes,
            'eating_yes': eating_yes,
    }
    return render(request, 'squirrel/statistics.html', context)
