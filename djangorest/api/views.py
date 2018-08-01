from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .serializers import BuildingSerializer, UnitSerializer
from .models import Building, Unit

class BuildingCreateView(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = Building.objects.all()
    serializer_class = BuildingSerializer

    def perform_create(self, serializer):
        """Save the post data when creating a new building."""
        serializer.save()
        
class BuildingDetailsView(generics.RetrieveUpdateDestroyAPIView):
    """This class handles the http GET, PUT and DELETE requests."""

    queryset = Building.objects.all()
    serializer_class = BuildingSerializer

class UnitCreateView(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = Unit.objects.all()
    serializer_class = UnitSerializer

    def perform_create(self, serializer):
        """Save the post data when creating a new unit."""
        serializer.save()
        
class UnitDetailsView(generics.RetrieveUpdateDestroyAPIView):
    """This class handles the http GET, PUT and DELETE requests."""

    queryset = Unit.objects.all()
    serializer_class = UnitSerializer
