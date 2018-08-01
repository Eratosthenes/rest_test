from rest_framework import serializers
from .models import Building

class BuildingSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Building
        fields = ('id', 
        	'name', 
        	'address', 
        	'capitalization_rate', 
        	'marketing',
        	'taxes',
        	'insurance',
        	'repairs',
        	'administration',
        	'payroll',
        	'utility',
        	'management',
        	'date_created', 
        	'date_modified')
        read_only_fields = ('date_created', 'date_modified')
