from django.shortcuts import render
from django.shortcuts import render_to_response
from appRegistration.forms import gymDetailsForm,memberDetailsForm
from django.http import HttpResponseRedirect
import datetime
from appRegistration.models import gymDetails, memberDetails
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from main.views import commonDisplay
# Create your views here.
# def dashboard(request):
# 	# obj=gymDetails.objects.filter(gymCity='Chennai')
# 	# print ('------')
# 	# print (obj.gymName)
# 	common=commonDisplay(request)
# 	print (common)
# 	return render(request,'base.html',context={})
	
@login_required
def clientRegistration(request):
	common=commonDisplay(request)
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
			save_it.gymUser_id=request.user.id
			if emptyDB:
				save_it.gymNumber=1
			else:
				save_it.gymNumber= int(latestGymNum['gymNumber'])+1
			form.save()
			return HttpResponseRedirect("/client/register/")
	common=commonDisplay(request)
	context={'form':form}
	finalContext={**common, **context} #append the dictionaries
	return render(request,'registerClient.html',context=finalContext)

@login_required
def memberRegistration(request):
	User = get_user_model()
	userId=User.id
	gymRegistered= False
	allGymNumbers=gymDetails.objects.all().values('gymUser_id')
	for i in allGymNumbers:
		print ('---------')
		print (i['gymUser_id'])
		print (request.user.id)
		if i['gymUser_id']==request.user.id:
			gymRegistered=True
	if not gymRegistered:
		return HttpResponseRedirect("/client/register/")

	form = memberDetailsForm(request.POST or None)
	emptyDB=True
	x=memberDetails.objects.all().values('memberNumber')
	gymObj=gymDetails.objects.filter(gymUser_id=request.user.id).values()
	for elements in gymObj:
		gymNumber=elements['gymNumber']
	
	for getMemberGymNum in x:
		emptyDB=False
		latestMemberNum=getMemberGymNum

	if request.POST:
		form= memberDetailsForm(request.POST)
		print ('inside post')
		if form.is_valid():
			print ('inside form')
			save_it=form.save(commit = False)
			save_it.memberRegistrationDate = datetime.datetime.now()
			save_it.memberGymNumber_id=gymNumber
			if emptyDB:
				save_it.memberNumber=1
			else:
				save_it.memberNumber= int(latestMemberNum['memberNumber'])+1
			form.save()
			return HttpResponseRedirect("/hello/")
	common=commonDisplay(request)
	context={'form':form}
	finalContext={**common, **context} #append the dictionaries
	return render(request,'registerMembers.html',context=finalContext)

def clientPlans(request):
	pass