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
