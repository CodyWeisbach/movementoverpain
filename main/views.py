# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import FeedbackForm

def index(request):
	form = FeedbackForm(request.POST or None)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		return redirect("thanks")
	context = {
	"title": "Choose Movement Over Pain",
	"form": form,
	}
	return render(request, "index.html", context)

def thanks(request):
	title = "Thanks! | Movement Over Pain"
	context = {
		"title": title,
	}
	return render(request, "thx.html", context)

def beta(request):
	title = "You are In! | Movement Over Pain"
	context = {
		"title": title,
	}
	return render(request, "beta.html", context)