from rest_framework import serializers
from .models import School, InventoryItem, Request

class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = '__all__'

class InventoryItemSerializer(serializers.ModelSerializer):
    school_name = serializers.CharField(source='school.name', read_only=True)
    
    class Meta:
        model = InventoryItem

        fields = ['id', 'name', 'description', 'quantity', 'unit', 'category', 'image', 'school_name', 'created_at']
        read_only_fields = ['school']

class RequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Request
        fields = '__all__'