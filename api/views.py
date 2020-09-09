from rest_framework import generics
from core_logic.models import Extend
from .serializers import  DateDetailSerializer, DateSerializer
from django.db.models import Sum


class DatePriceList(generics.ListAPIView):
    queryset = Extend.objects.all()
    serializer_class = DateSerializer


class DatePriceListDetail(generics.ListAPIView):
    serializer_class = DateDetailSerializer

    def get_queryset(self):
        identifier = self.kwargs['pk']
        return Extend.objects.filter(wallet__user__user__pk=identifier) \
            .values('date').annotate(price=Sum('price'))
