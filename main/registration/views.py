from django.shortcuts import render
from django.shortcuts import render_to_response
from registration.forms import gymDetailsForm
from django.http import HttpResponseRedirect
import datetime
from registration.models import gymDetails
# Create your views here.
def test(request):
	# obj=gymDetails.objects.filter(gymCity='Chennai')
	# print ('------')
	# print (obj.gymName)
	return render(request,'base.html',context={})

def clientRegistration(request):
	form = gymDetailsForm(request.POST or None)

	x=gymDetails.objects.all().values('gymNumber')
	for getLatestGymNum in x:
		latestGymNum=getLatestGymNum

	if request.POST:
		form= gymDetailsForm(request.POST)
		if form.is_valid():
			save_it=form.save(commit = False)
			save_it.gymRegistrationDate = datetime.datetime.now()
			save_it.gymNumber= int(latestGymNum['gymNumber'])+1
			form.save()
			return HttpResponseRedirect("/client/register/")
	return render(request,'registerClient.html',context={'form':form})