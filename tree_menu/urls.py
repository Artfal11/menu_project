from django.urls import path
from django.shortcuts import render

urlpatterns = [
    path('', lambda request: render(request, 'base.html'), name='home'),
    path('about/', lambda request: render(request, 'base.html'), name='about'),
    path('contact/', lambda request: render(request, 'base.html'), name='contact'),
    path('services/', lambda request: render(request, 'base.html'), name='services'),
    path('services/development/', lambda request: render(request, 'base.html'), name='services-development'),
]
