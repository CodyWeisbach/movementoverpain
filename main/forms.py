from django.forms import ModelForms, Textarea
from .models import Feedback

class FeedbackForm(forms.ModelForm):
	class Meta:
		model = Feedback
		fields = ("text")
		widgets = {
			'text': Textarea(attrs={'cols': 80, 'rows': 20})
		}