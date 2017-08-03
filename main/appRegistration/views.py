from django.shortcuts import render
from django.shortcuts import render_to_response
from appRegistration.forms import gymDetailsForm,memberDetailsForm,gymPlansForm,\
								memberActivatePlanForm, memberDetailsForm,staffDetailsForm,\
								UserDetailsForm
from django.http import HttpResponseRedirect
from datetime import datetime, timedelta
import datetime
from appRegistration.models import gymDetails, memberDetails,gymPlans,staffDetails
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from main.views import commonDisplay,activaPlans
from django.contrib import messages
from django.db.models import Q
import simplejson
# Create your views here.
def dashboard(request):
	gymObj=gymDetails.objects.filter(gymUser_id=request.user.id).values()
	for elements in gymObj:
		gymNumber=elements['gymNumber']
	totalNumberOfMembers=memberDetails.objects.filter(memberGymNumber_id=gymNumber).count()
	totalActiveMembers=memberDetails.objects.filter(memberGymNumber_id=gymNumber, memberStatus=1).count()
	newMembers=memberDetails.objects.filter(memberGymNumber_id=gymNumber, memberRegistrationDate__gte=datetime.datetime.now()-timedelta(days=30)).count()
	maleCount=memberDetails.objects.filter(memberGender='M',memberGymNumber_id=gymNumber).count()
	femaleCount=memberDetails.objects.filter(memberGender='F',memberGymNumber_id=gymNumber).count()

	# Start: Today's Stats calculation
	midnight=datetime.datetime.combine(datetime.datetime.today(), datetime.time(0))
	totalActiveStaff=staffDetails.objects.filter(staffGymNumber_id=gymNumber,staffStatus=1).count()
	today_newMembers=memberDetails.objects.filter(memberRegistrationDate__gte=(midnight),memberGymNumber_id=gymNumber,).count()
	today_maleCount=memberDetails.objects.filter(memberRegistrationDate__gte=(midnight),memberGender='M',memberGymNumber_id=gymNumber).count()
	today_femaleCount=memberDetails.objects.filter(memberRegistrationDate__gte=(midnight),memberGender='F',memberGymNumber_id=gymNumber).count()
	common=commonDisplay(request)
	context={'totalNumberOfMembers':totalNumberOfMembers,'totalActiveMembers':totalActiveMembers,
			'newMembers':newMembers,'maleCount':maleCount,'femaleCount':femaleCount,'totalActiveStaff':totalActiveStaff,
			'today_newMembers':today_newMembers,'today_maleCount':today_maleCount,'today_femaleCount':today_femaleCount}
	finalContext={**common, **context} #append the dictionaries
	return render(request,'dashboard.html',context=finalContext)
	
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
			try:
				form.save()
				messages.success(request,'SUCCESS! Business Successfully Registered', extra_tags='success')
			except:
				messages.error(request,'ERROR! Your have already registered a business in our system',extra_tags='warning')
			return HttpResponseRedirect("/client/register/")
	common=commonDisplay(request)
	context={'form':form}
	finalContext={**common, **context} #append the dictionaries
	return render(request,'registerClient.html',context=finalContext)	

@login_required
def memberRegistration(request):
	# Start: Ensure Gym is registered first
	User = get_user_model()
	userId=User.id
	gymRegistered= False
	allGymNumbers=gymDetails.objects.all().values('gymUser_id')
	for i in allGymNumbers:
		if i['gymUser_id']==request.user.id:
			gymRegistered=True
	if not gymRegistered:
		return HttpResponseRedirect("/client/register/")
	# End
	form = memberDetailsForm(request.POST or None)
	emptyDB=True
	x=memberDetails.objects.all().values('memberNumber')
	gymObj=gymDetails.objects.filter(gymUser_id=request.user.id).values()
	for elements in gymObj:
		gymNumber=elements['gymNumber']
	latestMemberNum=0
	for getMemberGymNum in x:
		print ('getMemberGymNum is:',getMemberGymNum)
		emptyDB=False
		latestMemberNum=latestMemberNum+1
	
	if request.POST:
		form= memberDetailsForm(request.POST)
		print ('inside post')
		print (request.POST['selectedPlanName'])
		print (request.POST['memberContactNumber'])

		if form.is_valid():
			checkAlreadyRegistered= memberDetails.objects.filter(memberGymNumber_id=gymNumber,
																memberContactNumber=request.POST['memberContactNumber'])
			if checkAlreadyRegistered:
				print ('Already registered')
				messages.success(request,'ERROR: Member Already registered')
				return HttpResponseRedirect("/member/register/")
			# for i in checkAlreadyRegistered:
			# 	print (i['memberContactNumber'])
			# 	if int(i['memberContactNumber']) == int(request.POST['memberContactNumber']):
			# 		print ('Already registered')
			# 		messages.success(request,'ERROR: Member Already registered')
			# 		return HttpResponseRedirect("/member/register/")
			print ('inside form')
			save_it=form.save(commit = False)
			save_it.memberRegistrationDate = datetime.datetime.now()
			save_it.memberGymNumber_id = gymNumber
			save_it.memberPlanActivationDate = datetime.datetime.now()
			save_it.memberPlan=request.POST['selectedPlanName']
			Plans=gymPlans.objects.filter(planGymNumber_id=gymNumber,planName=request.POST['selectedPlanName']).values()
			print ('****')
			print (Plans)
			for i in Plans:
				expiryDuration=i['planDuration']
			save_it.memberPlandExpiryDate= datetime.datetime.now() + datetime.timedelta(days=expiryDuration)
			if emptyDB:
				save_it.memberNumber=1
			else:
				print ('---')
				print (latestMemberNum)
				save_it.memberNumber= latestMemberNum+1
			form.save()
			messages.success(request,'Member Registration Successful!')
			return HttpResponseRedirect("/member/register/")
	common=commonDisplay(request)
	activePlans=activaPlans(request)
	context={'form':form}
	finalContext={**common, **context,**activePlans} #append the dictionaries
	return render(request,'registerMembers.html',context=finalContext)

@login_required
def staffRegistration(request):
	# Start: Ensure Gym is registered first
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
	# End
	form = staffDetailsForm(request.POST or None)
	emptyDB=True
	x=staffDetails.objects.all().values('staffNumber')
	gymObj=gymDetails.objects.filter(gymUser_id=request.user.id).values()
	for elements in gymObj:
		gymNumber=elements['gymNumber']
	latestMemberNum=0
	for getMemberGymNum in x:
		print ('getMemberGymNum is:',getMemberGymNum)
		emptyDB=False
		latestMemberNum=latestMemberNum+1

	if request.POST:
		form= staffDetailsForm(request.POST)
		print ('inside post')
		if form.is_valid():
			print ('inside form')
			save_it=form.save(commit = False)
			save_it.staffRegistrationDate = datetime.datetime.now()
			save_it.staffGymNumber_id=gymNumber
			if emptyDB:
				save_it.staffNumber=1
			else:
				print ('---')
				print (latestMemberNum)
				save_it.staffNumber= latestMemberNum+1
			form.save()
			messages.success(request,'Staff Registration Successful')
			return HttpResponseRedirect("/staff/register/")
	common=commonDisplay(request)
	context={'form':form}
	finalContext={**common, **context} #append the dictionaries
	return render(request,'registerStaffs.html',context=finalContext)

def clientPlans(request):
	# Start: Ensure Gym is registered first
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
	# End
	common=commonDisplay(request)
	form = gymPlansForm(request.POST or None)
	if request.POST:
		if form.is_valid():
			save_it=form.save(commit = False)
			gymObj=gymDetails.objects.filter(gymUser_id=request.user.id).values()
			for elements in gymObj:
				gymNumber=elements['gymNumber']
				save_it.planGymNumber_id= gymNumber
			form.save()
			print ('SAVED!!!!!!!!!')
			return HttpResponseRedirect("/client/plans/")
	common=commonDisplay(request)
	context={'form':form}
	finalContext={**common, **context} #append the dictionaries
	return render(request,'clientPlans.html',context=finalContext)

def clientActivatePlan(request):
	
	form = memberActivatePlanForm(request.POST or None)
	context={'form':form,'buttontext':'Submit'}

	if form.is_valid():
		print ('******')
		input=form.cleaned_data['searchUser']
		print (input)
		gymObj=gymDetails.objects.filter(gymUser_id=request.user.id).values()
		for i in gymObj:
			gymNumber= i['gymNumber']
		member=memberDetails.objects.filter(memberContactNumber=input, memberGymNumber_id=gymNumber).values()
		if not member:
			messages.error(request,'ERROR! Number not registered in system. Please check the number entered.')
		if 'selectedPlanName' in request.POST:
				print ('lllllllllllllll')
				print (request.POST['selectedPlanName'])
				gymObj=gymDetails.objects.filter(gymUser_id=request.user.id).values()
				for elements in gymObj:
					gymNumber=elements['gymNumber']
				Plans=gymPlans.objects.filter(planGymNumber_id=gymNumber,planName=request.POST['selectedPlanName']).values()
				print ('****')
				print (Plans)
				for i in Plans:
					expiryDuration=i['planDuration']
					print ('.............')
					print (expiryDuration)
				
				userData=memberDetails.objects.filter(memberContactNumber=input,
													 memberGymNumber_id=gymNumber).update(
													 memberPlanActivationDate=datetime.datetime.now(),
													 memberPlan=request.POST['selectedPlanName'],
													 memberPlandExpiryDate=datetime.datetime.now() + timedelta(days=expiryDuration))
				messages.success(request,'Updated successfully')
		for i in member:
			name=i['memberName']
			memberEmail=i['memberEmail']
			registrationDate=i['memberRegistrationDate']
			status=i['memberStatus']
			memberId=i['memberGymNumber_id']
			activeMemberPlan=i['memberPlan']
			memberPlanActivationDate=i['memberPlanActivationDate']
			memberPlandExpiryDate=i['memberPlandExpiryDate']	
			buttontext='Update'		

			context={'form':form,'name':name,'memberEmail':memberEmail,'registrationDate':registrationDate,
					'status':status,'memberId':memberId,'activeMemberPlan':activeMemberPlan,'memberPlanActivationDate':memberPlanActivationDate,
					'memberPlandExpiryDate':memberPlandExpiryDate,'buttontext':buttontext}

	common=commonDisplay(request)
	activePlans=activaPlans(request)

	finalContext={**common, **context,**activePlans} #append the dictionaries
	return render(request,'gymPlans.html',context=finalContext)

