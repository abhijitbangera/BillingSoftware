from django import forms
from registration.models import gymDetails

class gymDetailsForm(forms.ModelForm):

	class Meta:
		model= gymDetails
		fields = '__all__'
		exclude = ['gymRegistrationDate','gymNumber']