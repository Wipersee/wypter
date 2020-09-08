from rest_framework import serializers
from core_logic.models import Extend, Category, Wallet
from account.models import Profile


class PriceCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Extend
        fields = ('price', 'wallet')


class CategotySerializer(serializers.ModelSerializer):
    price = PriceCategorySerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ('name', 'price')


class DateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Extend
        fields = ('date', 'price', 'wallet')

