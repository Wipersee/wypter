from django.urls import path
from .views import DatePriceList, DatePriceListDetail


urlpatterns = [
    path('graph_chart/', DatePriceList.as_view(), name='graphgraph_chart_list'),
    path('graph_chart/<int:pk>/', DatePriceListDetail.as_view(), name='detail_user_income')
]