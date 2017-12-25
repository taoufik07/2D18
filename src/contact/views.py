from django.shortcuts import render, redirect
from django.urls import reverse

from .forms import ContactForm


def contact(request):
	if request.method == "POST":
		form = ContactForm(request.POST)
		if form.is_valid():
			form.save()
	return redirect(reverse("home:home")+"#contact")
