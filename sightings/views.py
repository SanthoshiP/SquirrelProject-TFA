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
    total_count = Chipmunk.objects.all().count()
    age_juvenile = Chipmunk.objects.filter(age='Juvenile').count()
    age_adult = Chipmunk.objects.filter(age='Adult').count()
    location_above = Chipmunk.objects.filter(location='Above Ground').count()
    location_plane = Chipmunk.objects.filter(location='Ground Plane').count()
    running_true = Chipmunk.objects.filter(running=True).count()
    #running_false = Squirrels.objects.filter(running=False).count()
    eating_true = Chipmunk.objects.filter(eating=True).count()
    approach_true = Chipmunk.objects.filter(approaches=True).count()
    context = {
            'total_count':total_count,
            'age_juvenile': age_juvenile,
            'age_adult': age_adult,
            'location_above': location_above,
            'location_plane': location_plane,
            'running_true': running_true,
            'eating_true': eating_true,
            'approach_true': approach_true,
    }
    return render(request, 'squirrel/statistics.html', context)
