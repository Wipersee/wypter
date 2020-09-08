from django.urls import path
from .views import DatePriceList, DatePriceListDetail


urlpatterns = [
    path('pie_chart/', DatePriceList.as_view(), name='pie_chart_list'),
    path('pie_chart/<int:pk>/', DatePriceListDetail.as_view(), name='pie_chart'),
]