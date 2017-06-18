from django.db import models

# Create your models here.
class gymDetails(models.Model):
	gymName=models.CharField(max_length=100)
	gymCity=models.CharField(max_length=100)
	gymAddress=models.TextField()
	gymPincode=models.IntegerField(max_length=9)
	gymRegistrationDate=models.DateTimeField('Registration Date')
	gymNumber=models.IntegerField(max_length=9)

	def __unicode__(self):
		return self.gymNumber
