from django import forms
from django.forms import ModelForm, Textarea
#from django.utils.translation import ugettext_lazy as _
from .models import Feedback

class FeedbackForm(forms.ModelForm):
	class Meta:
		model = Feedback
		fields = ('text',)
		labels = {
			"text": "Just fill out the form below."
		}
		widgets = {
			'text': Textarea(attrs={'cols': 80, 'rows': 20})
		}