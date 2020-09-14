from django.urls import path
from . import views

urlpatterns = [
    path('dashbord/', views.dashboard, name='dashboard'),
    path('pie_chart/', views.pie_chart, name='pie_chart'),
    path('graph_chart/', views.graph_chart, name='graph_chart'),
    path('graph_chart/detail_sum/', views.detail_sum, name='detail_sum')
]
