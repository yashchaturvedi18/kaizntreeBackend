# serializers.py

from rest_framework import serializers
from .models import Item
from django.contrib.auth.models import User

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

    class Meta:
        model = User
        fields = ['username', 'password']

class ItemCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ['name', 'sku', 'category', 'tags', 'stock_status', 'available_stock']