from django.urls import path
from . import views
from django.conf.urls.static import static
from custom_login import settings
from custom_auth import views as cust_views


app_name = 'employee'


urlpatterns = [
    path('add_employee/', views.add_employee.as_view(), name='add_employee'),

    path('', views.Dashboard, name='dashboard'),
    path('(?P<pk>\d+)/', views.profile, name='profile'),
    path('employee', views.profile, name='profile'),
    path('(?P<pk>\d+)/', views.profile, name='profile'),


    path('(?P<pk>\d+)/update', views.edit_employee.as_view(), name='edit_employee'),
    path('(?P<pk>\d+)/delete', views.delete_employee.as_view(), name='delete_employee'),

    path('(?P<pk>\d+)/view_pdf', views.view_pdf, name='view_pdf'),






]
