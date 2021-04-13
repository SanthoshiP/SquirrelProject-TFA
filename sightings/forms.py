from django.forms import ModelForm

from squirrel.models import Chipmunk

class Form(ModelForm):
    class Meta:
        model = Chipmunk
        fields = '__all__'
