from django.conf.urls import url,include
from django.contrib import admin
from . import views

urlpatterns = [
				url(r'^dashboard/$', views.dashboard,name='dashboard'),
				url(r'^accounts/', include('registration.backends.simple.urls')), 
				# url(r'^accounts/', include('registration.backends.hmac.urls')),
				url(r'^client/register/$', views.clientRegistration, name='clientRegistration'),
				url(r'^client/plans/$', views.clientPlans, name='clientPlans'),
				url(r'^client/activateplan/$', views.clientActivatePlan, name='clientActivatePlan'),
				url(r'^member/register/$', views.memberRegistration, name='memberRegistration'),
				url(r'^staff/register/$', views.staffRegistration, name='staffRegistration'),
				url(r'^$', views.dashboard),
				url(r'^export/csv/$', views.export_users_csv, name='export_users_csv'),
				url(r'^export/csv2/$', views.export_monthly_report, name='export_monthly_report'),
				url(r'^export/csv3/$', views.current_month_income, name='current_month_income'),
				url(r'^export/csv4/$', views.last_month_income, name='last_month_income'),
				url(r'^export/csv5/$', views.total_income, name='total_income'),
				url(r'^usersearch/$',views.usersearch,name='usersearch'),
				url(r'^staffsearch/$',views.staffsearch,name='staffsearch'),
				url(r'^member/edit/$',views.edituser,name='edituser'),
				url(r'^client/edit/$', views.clientEdit, name='clientEdit'),
				url(r'^client/plandeactivate/$', views.deactivePlan, name='deactivePlan'),
				url(r'^client/editStaff/$', views.deactiveStaff, name='deactiveStaff'),


			   ]
