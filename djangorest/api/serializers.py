from rest_framework import serializers
from .models import Building, Unit, Loan

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

class UnitSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Unit
        fields = ('id', 
        	'building_id', 
			'unit_number',
			'monthly_rent',
			'vacancy',
			'bedrooms',
			'bathrooms',
			'date_created',
        	'date_modified')
        read_only_fields = ('date_created', 'date_modified')

class LoanSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Loan
        fields = ('id', 
        	'building_id', 
			'loan_amount',
			'debt_rate',
			'date_created',
        	'date_modified')
        read_only_fields = ('date_created', 'date_modified')

