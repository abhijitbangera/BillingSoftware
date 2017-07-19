from django import forms
from appRegistration.models import gymDetails,memberDetails,gymPlans

class gymDetailsForm(forms.ModelForm):

	class Meta:
		model= gymDetails
		fields = '__all__'
		exclude = ['gymRegistrationDate','gymNumber','gymUser']

class memberDetailsForm(forms.ModelForm):

	class Meta:
		model= memberDetails
		fields = '__all__'
		exclude = ['memberStatus','memberNumber','memberRegistrationDate','memberGymNumber']

class gymPlansForm(forms.ModelForm):
	class Meta:
		model= gymPlans
		fields = '__all__'
		exclude=['planGymNumber']

class memberActivatePlanForm(forms.Form):
    searchUser = forms.CharField(required=True)

# class memberDetailsForm(forms.Form):
# 	memberName = forms.CharField(required=True)
# 	memberContactNumber = forms.CharField(required=True)
	
  