from django import forms
from appRegistration.models import gymDetails,memberDetails,gymPlans,staffDetails


class gymDetailsForm(forms.ModelForm):
	class Meta:
		model= gymDetails
		fields = '__all__'
		exclude = ['gymRegistrationDate','gymNumber','gymUser']


class memberDetailsForm(forms.ModelForm):
	class Meta:
		model= memberDetails
		fields = '__all__'
		exclude = ['memberStatus','memberNumber','memberRegistrationDate','memberGymNumber',
					'memberPlanActivationDate','memberPlandExpiryDate','memberPlan']


class gymPlansForm(forms.ModelForm):
	class Meta:
		model= gymPlans
		fields = '__all__'
		exclude=['planGymNumber']


class memberActivatePlanForm(forms.Form):
    searchUser = forms.CharField(required=True)

	
class staffDetailsForm(forms.ModelForm):
	class Meta:
		model= staffDetails
		fields = '__all__'
		exclude = ['staffStatus','staffNumber','staffRegistrationDate','staffGymNumber']


class UserDetailsForm(forms.Form):
    name = forms.CharField(max_length=300)
    email = forms.CharField(max_length=300)
