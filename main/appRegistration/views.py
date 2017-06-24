from django.shortcuts import render
from django.shortcuts import render_to_response
from appRegistration.forms import gymDetailsForm,memberDetailsForm
from django.http import HttpResponseRedirect
import datetime
from appRegistration.models import gymDetails
from django.contrib.auth.decorators import login_required
# Create your views here.
def test(request):
	# obj=gymDetails.objects.filter(gymCity='Chennai')
	# print ('------')
	# print (obj.gymName)
	return render(request,'base.html',context={})

@login_required
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

def memberRegistration(request):
	form = memberDetailsForm(request.POST or None)
	return render(request,'registerMembers.html',context={'form':form})

def clientLogin(request):
	
	return render(request,'base_login.html',context={})