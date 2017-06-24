from django.db import models

# Create your models here.
class gymDetails(models.Model):
	gymName=models.CharField(max_length=100)
	gymCity=models.CharField(max_length=100)
	gymAddress=models.TextField()
	gymPincode=models.IntegerField(max_length=9)
	gymRegistrationDate=models.DateTimeField('Registration Date')
	gymNumber=models.IntegerField(max_length=9,primary_key=True, null=False)
	gymUsername=models.CharField(max_length=100)
	gymPassword=models.CharField(max_length=100)

	def __str__(self):
		return str(self.gymNumber)

class memberDetails(models.Model):
	memberName=models.CharField(max_length=100)
	memberCity=models.CharField(max_length=100)
	memberAddress=models.TextField(blank=True)
	memberPincode=models.IntegerField(max_length=9,blank=True)
	memberContactNumber=models.IntegerField(max_length=14)
	memberEmergencyNumber=models.IntegerField(max_length=14,blank=True)
	memberEmail=models.CharField(max_length=100)
	memberRegistrationDate=models.DateTimeField('Registration Date')
	memberNumber=models.IntegerField(max_length=9,primary_key=True, null=False)

	def __str__(self):
		return str(self.memberNumber)