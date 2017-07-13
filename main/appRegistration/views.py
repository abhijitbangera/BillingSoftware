from django.shortcuts import render
from django.shortcuts import render_to_response
from appRegistration.forms import gymDetailsForm,memberDetailsForm
from django.http import HttpResponseRedirect
import datetime
from appRegistration.models import gymDetails, memberDetails
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
	emptyDB=True
	x=gymDetails.objects.all().values('gymNumber')
	for getLatestGymNum in x:
		emptyDB=False
		latestGymNum=getLatestGymNum

	if request.POST:
		form= gymDetailsForm(request.POST)
		if form.is_valid():
			save_it=form.save(commit = False)
			save_it.gymRegistrationDate = datetime.datetime.now()
			if emptyDB:
				save_it.gymNumber=1
			else:
				save_it.gymNumber= int(latestGymNum['gymNumber'])+1
			form.save()
			return HttpResponseRedirect("/client/register/")
	return render(request,'registerClient.html',context={'form':form})

@login_required
def memberRegistration(request):
	form = memberDetailsForm(request.POST or None)
	x=memberDetails.objects.all().values('memberNumber')
	for getMemberGymNum in x:
		latestMemberNum=getMemberGymNum

	if request.POST:
		form= memberDetailsForm(request.POST)
		print ('inside post')
		if form.is_valid():
			print ('inside form')
			save_it=form.save(commit = False)
			save_it.memberRegistrationDate = datetime.datetime.now()
			save_it.memberNumber= int(latestMemberNum['memberNumber'])+1
			form.save()
			return HttpResponseRedirect("/hello/")
	return render(request,'registerMembers.html',context={'form':form})

def clientLogin(request):
	
	return render(request,'base_login.html',context={})