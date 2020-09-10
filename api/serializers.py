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


class ExtendSerializer(serializers.ModelSerializer):
    class Meta:
        model = Extend
        fields = ('price', 'wallet')

class CategorySerializer(serializers.ModelSerializer):
    category_name = ExtendSerializer(many=True,  read_only=True)
    class Meta:
        model = Category
        fields = ('name', 'category_name')
