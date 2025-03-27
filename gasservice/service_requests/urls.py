from django.urls import path
from service_requests import views

app_name = 'service_requests'

urlpatterns = [
    path('', views.home, name='home'),
    path('submit/', views.submit_request, name='submit_request'),
    path('track/', views.list_requests, name='list_requests'),
    path('track/<int:request_id>/', views.track_request, name='track_request'),
]
