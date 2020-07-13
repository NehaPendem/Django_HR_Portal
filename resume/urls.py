from django.urls import path
from . import views
from django.conf.urls.static import static


app_name = 'resume'

urlpatterns = [
    path('', views.showform.as_view(), name='addresume'),
    path('test/', views.success, name='test'),

]
