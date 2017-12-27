from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages

from contact.forms import ContactForm
	
from .forms import RegisterForm
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
		'register_form': RegisterForm(),
	}
	return render(request, 'home.html', context)



def register(request):
	if request.method == "POST":
		form = RegisterForm(request.POST)
		if form.is_valid():
			form.save()
			messages.success(request, 'Successfuly registred')
		else:
			context = {
				'site_info': SiteInfo.objects.first(),
				'attandants': Attandant.objects.all(),
				'morning_programs': OurProgram.objects.filter(time__lte="12:00"),
				'noon_programs': OurProgram.objects.filter(time__gt="12:00"),
				'faq': FAQ.objects.all(),
				'sponsors': Sponsor.objects.all(),
				'contact_form': ContactForm(),
				'register_form': form,
				'anchor' : 'register'
			}
			return render(request, 'home.html', context)
	return redirect(reverse("home:home")+"#register")