# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Feedback(models.Model):
	text = models.CharField(max_length=1000)
	timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)