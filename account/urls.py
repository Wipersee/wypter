from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.registration, name="registration"),
    path('', include('django.contrib.auth.urls')),
    path('settings/', views.settings, name='settings'),
]
