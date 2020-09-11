from rest_framework import generics
from core_logic.models import Extend, Category, Wallet
from account.models import Profile
from .serializers import  DateDetailSerializer, DateSerializer, CategorySerializer, ExtendSerializer
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


class CategoryPriceDetail(generics.ListAPIView):
    serializer_class = ExtendSerializer

    def get_queryset(self):
        identifier = self.kwargs['pk']
        wallet = Wallet.objects.get(user=Profile.objects.get(user=identifier))
        return Extend.objects.filter(wallet=wallet)

class CategoryPriceList(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer