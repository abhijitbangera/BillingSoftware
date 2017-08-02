from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class memberDetails(models.Model):
	memberName=models.CharField(max_length=100)
	GENDER_CHOICES = (('M', 'Male'),('F', 'Female'),)
	memberGender = models.CharField(max_length=1, choices=GENDER_CHOICES)
	memberCity=models.CharField(max_length=100)
	memberAddress=models.TextField(blank=True)
	memberPincode=models.IntegerField(max_length=9,blank=True)
	memberContactNumber=models.IntegerField(max_length=14)
	memberEmergencyNumber=models.IntegerField(max_length=14,blank=True)
	memberEmail=models.CharField(max_length=100)
	memberRegistrationDate=models.DateTimeField('Registration Date')
	memberNumber=models.IntegerField(max_length=9,primary_key=True, null=False)
	memberStatus=models.BooleanField(default=True)
	memberPlan=models.CharField(max_length=100)
	memberPlanActivationDate=models.DateTimeField('Plan Activation Date')
	memberPlandExpiryDate=models.DateTimeField('Plan Expiry Date')
	memberGymNumber=models.ForeignKey('gymDetails')

	def __str__(self):
		return str(self.memberNumber)

class gymDetails(models.Model):
	gymName=models.CharField(max_length=100)
	gymCity=models.CharField(max_length=100)
	gymAddress=models.TextField()
	gymPincode=models.IntegerField(max_length=9)
	gymRegistrationDate=models.DateTimeField('Registration Date')
	gymNumber=models.IntegerField(max_length=9,primary_key=True, null=False)
	gymUsername=models.CharField(max_length=100)
	gymPassword=models.CharField(max_length=100)
	gymUser=models.ForeignKey(User, unique=True)

	def __str__(self):
		return str(self.gymNumber)

class gymPlans(models.Model):
	planName=models.CharField(max_length=100)
	planDuration=models.IntegerField(max_length=4,blank=False, null=False)
	planPrice=models.IntegerField(max_length=9,blank=False, null=False)
	planDescription=models.CharField(max_length=300)
	planGymNumber=models.ForeignKey('gymDetails')

	def __str__(self):
		return str(self.planName+self.planGymNumber)


class staffDetails(models.Model):
	staffName=models.CharField(max_length=100)
	GENDER_CHOICES = (('M', 'Male'),('F', 'Female'),)
	staffGender = models.CharField(max_length=1, choices=GENDER_CHOICES)
	staffCity=models.CharField(max_length=100)
	staffAddress=models.TextField(blank=True)
	staffPincode=models.IntegerField(max_length=9,blank=True)
	staffContactNumber=models.IntegerField(max_length=14)
	staffEmergencyNumber=models.IntegerField(max_length=14,blank=True)
	staffEmail=models.CharField(max_length=100)
	staffRegistrationDate=models.DateTimeField('Registration Date')
	staffNumber=models.IntegerField(max_length=9,primary_key=True, null=False)
	staffStatus=models.BooleanField(default=True)
	staffGymNumber=models.ForeignKey('gymDetails')

	def __str__(self):
		return str(self.staffNumber)