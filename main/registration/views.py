from django.shortcuts import render
from django.shortcuts import render_to_response
from registration.forms import gymDetailsForm
from django.http import HttpResponseRedirect


# Create your views here.
def test(request):
	return render(request,'base.html',context={})

def clientRegistration(request):
	if request.POST:
		form= gymDetailsForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect("/weighttracker/")
	return render(request,'registerClient.html',context={})