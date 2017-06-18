from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
				url(r'^dashboard/$', views.test),
				url(r'^client/register/$', views.clientRegistration, name='clientRegistration'),

			   ]
