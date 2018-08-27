# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.shortcuts import render

def index(request):
	context = {
	"title": "Choose Movement Over Pain"
	}
	return render(request, "index2.html", context)


