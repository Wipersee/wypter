from django.urls import path
from .views import DatePriceList, DatePriceListDetail, CategoryPriceList, CategoryPriceDetail


urlpatterns = [
    path('graph_chart/', DatePriceList.as_view(), name='graph_chart_list'),
    path('graph_chart/<int:pk>/', DatePriceListDetail.as_view(), name='detail_user_income'),
    path('pie_chart/', CategoryPriceList.as_view(), name='pie_chart_list'),
    path('pie_chart/<int:pk>/', CategoryPriceDetail.as_view(), name='detail_user_category')
]