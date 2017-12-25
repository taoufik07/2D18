from django.shortcuts import render

from contact.forms import ContactForm
	
from .models import *


def home(request):

	context = {
		'site_info': SiteInfo.objects.first(),
		'attandants': Attandant.objects.all(),
		'morning_programs': OurProgram.objects.filter(time__lte="12:00"),
		'noon_programs': OurProgram.objects.filter(time__gt="12:00"),
		'faq': FAQ.objects.all(),
		'sponsors': Sponsor.objects.all(),
		'contact_form': ContactForm(),
	}
	return render(request, 'home.html', context)