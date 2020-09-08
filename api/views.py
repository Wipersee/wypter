from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics
from core_logic.models import Extend, Category
from .serializers import DateSerializer
from account.models import Profile


class DatePriceList(generics.ListAPIView):
    queryset = Extend.objects.all()
    serializer_class = DateSerializer


class DatePriceListDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Extend.objects.all()
    serializer_class = DateSerializer


