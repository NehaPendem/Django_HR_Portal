from django.urls import path
from . import views
from employee import views as emp_views

app_name = 'custom_auth'

urlpatterns = [
    path('signup/', views.SignupView.as_view(), name='signup'),
    path('dashboard/', views.Dashboard, name='dashboard'),

    path('view_filter', emp_views.show_filtered_emp, name='show_filtered_emp'),
    path('', views.LoginView.as_view(), name='login'),

    path('home/', views.Homepage, name='home'),
    path('logout/', views.Logout, name='logout'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('add_employee', emp_views.add_employee.as_view(), name='add_employee'),
    path('filter_employees', emp_views.filter_employees, name='filter_employees'),
    path('edit_employee', emp_views.edit_employee.as_view(), name='edit_employee'),
    path('profile', emp_views.profile, name='profile'),
]
