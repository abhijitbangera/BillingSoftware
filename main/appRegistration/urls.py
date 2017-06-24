from django.conf.urls import url,include
from django.contrib import admin
from . import views

urlpatterns = [
				url(r'^dashboard/$', views.test),
				url(r'^accounts/', include('registration.backends.simple.urls')), 
				# url(r'^accounts/', include('registration.backends.hmac.urls')),
				url(r'^client/register/$', views.clientRegistration, name='clientRegistration'),
				url(r'^member/register/$', views.memberRegistration, name='memberRegistration'),
				url(r'^client/login/$', views.clientLogin, name='clientLogin'),

			   ]
