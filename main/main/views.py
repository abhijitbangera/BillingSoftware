from django.shortcuts import render
from django.contrib.auth.models import User
from appRegistration.models import gymDetails,gymPlans

def commonDisplay(request):
	user = request.user.username
	userId=request.user.id
	print (userId)
	gymName=''
	gymNumber='#'
	gymObj=gymDetails.objects.filter(gymUser_id=request.user.id).values()
	for i in gymObj:
		gymName=i['gymName']
		gymNumber=i['gymNumber']
		print (gymName,gymNumber)
	context={'user':user,'userId':userId,'gymName':gymName,'gymNumber':gymNumber}
	return context
	# return render(request,'base.html',context=context)
	# return user,userId,gymName,gymNumber

def activaPlans(request):
	gymObj=gymDetails.objects.filter(gymUser_id=request.user.id).values()
	for i in gymObj:
		gymNumber= i['gymNumber']

	Plans=gymPlans.objects.filter(planGymNumber_id=gymNumber).values()
	planNames=['None']
	planDuration=['None']
	planPrice=['None']
	planDescription=['None']
	plans_as_dict=[]
	for names in Plans:
		planNames.append(names['planName'])
		planDuration.append(names['planDuration'])
		planPrice.append(names['planPrice'])
		planDescription.append(names['planDescription'])
		song_as_dict = {
			            'planNames' : names['planName'],
			            'planDuration' : names['planDuration'],
			            'planPrice' : names['planPrice'],
			            'planDescription':names['planDescription']}
		plans_as_dict.append(song_as_dict)
	# simplejson.dumps(plans_as_dict)
	# print ('planNames:', planNames)
	# print ('planDuration:', planDuration)
	# print ('planPrice:', planPrice)
	# print ('planDescription:', planDescription)
	# print ('-----------')
	plans_as_dict=(plans_as_dict)
	context={'plans_as_dict':plans_as_dict}
	return context