from django.urls import path, include
from . import views

urlpatterns=[
    path('', views.dashboard, name='dashboard'),
    path('pie_chart/', views.pie_chart, name='pie_chart'),
    path('graph_chart/', views.graph_chart, name='graph_chart'),
]