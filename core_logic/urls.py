from django.urls import path
from . import views

urlpatterns = [
    path('dashbord/', views.dashboard, name='dashboard'),
    path('pie_chart/', views.pie_chart, name='pie_chart'),
    path('graph_chart/', views.graph_chart, name='graph_chart'),
    path('detail_sum/', views.detail_sum, name='detail_sum'),
    path('detail_sum/delete/<int:pk>/', views.delete_extend, name='delete_extend'),
    path('detail_sum/update/<int:pk>/', views.extend_update, name='extend_update'),
    path('monthly_extend_add/', views.monthly_extend, name='monthly_extends'),
]
