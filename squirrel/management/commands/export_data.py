import csv
	from django.core.management.base import BaseCommand, CommandError
	#from django.apps import apps
	

	from squirrel.models import Chipmunk
	

	class Command(BaseCommand):
	    help = ("Output the specified model as csv")
	

	    def add_arguments(self, parser):
	        parser.add_argument('args',type=str,nargs='*')
	

	    def handle(self,*args,**kwargs):
	        #path = args[0]
	        #fields = Chipmunk._meta.fields
	        
	        #model = apps.get_model('map','Chipmunk')
	        field_names = [f.name for f in Chipmunk._meta.fields]
	        filename = args[0]
	

	        with open(filename, 'w') as fp:
	            writer = csv.writer(fp, delimiter = ',')
	            writer.writerow(field_names)
	

	            for instance in Chipmunk.objects.all():
	                writer.writerow([str(getattr(instance,f)) for f in field_names])

