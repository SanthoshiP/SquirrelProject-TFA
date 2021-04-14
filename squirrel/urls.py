from django.urls import path
from squirrel.views import map
from . import views

urlpatterns = [
    path('', views.map,name='map'),
]
