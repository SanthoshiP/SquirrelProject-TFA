from django.urls import path

from . import views
from sightings.views import edit_sightings, add_sightings, stats

urlpatterns = [
    path('', views.list_of_squirrels),
    path('<unique_squirrel_id>/', views.edit_sightings, name='edit_sightings'),
    path('add/', views.add_sightings, name='add_sightings'),    
    path('stats/', views.stats, name = 'stats'),    
    ]