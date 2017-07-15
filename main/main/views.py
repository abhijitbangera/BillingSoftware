from django.shortcuts import render
from django.contrib.auth.models import User
from appRegistration.models import gymDetails

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