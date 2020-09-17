from rest_framework import serializers
from core_logic.models import Extend, Category, Wallet
from account.models import Profile


class DateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Extend
        fields = ('date', 'price', 'wallet')


class DateDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Extend
        fields = ('date', 'price')

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('name',)

class ExtendSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    class Meta:
        model = Extend
        fields = ('price', 'category')
