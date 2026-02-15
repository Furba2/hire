from django.urls import path
from . import views

app_name = 'Hire'

urlpatterns = [

    path('', views.index, name='index'),

    path('services/', views.services, name='services'),

    path('services/<int:service_id>/', views.service,
    name='service'),
    
]