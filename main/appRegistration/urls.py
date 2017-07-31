from django.conf.urls import url,include
from django.contrib import admin
from . import views

urlpatterns = [
				url(r'^dashboard/$', views.dashboard),
				url(r'^accounts/', include('registration.backends.simple.urls')), 
				# url(r'^accounts/', include('registration.backends.hmac.urls')),
				url(r'^client/register/$', views.clientRegistration, name='clientRegistration'),
				url(r'^client/plans/$', views.clientPlans, name='clientPlans'),
				url(r'^client/activateplan/$', views.clientActivatePlan, name='clientActivatePlan'),
				url(r'^member/register/$', views.memberRegistration, name='memberRegistration'),
				url(r'^staff/register/$', views.staffRegistration, name='staffRegistration'),


			   ]
