from django import forms
from appRegistration.models import gymDetails,memberDetails

class gymDetailsForm(forms.ModelForm):

	class Meta:
		model= gymDetails
		fields = '__all__'
		exclude = ['gymRegistrationDate','gymNumber']

class memberDetailsForm(forms.ModelForm):

	class Meta:
		model= memberDetails
		fields = '__all__'
		exclude = ['memberStatus','memberNumber','memberRegistrationDate']
