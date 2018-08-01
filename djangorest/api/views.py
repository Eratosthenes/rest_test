from django.shortcuts import render, get_object_or_404
import pdb

# Create your views here.
from rest_framework import generics
from .serializers import BuildingSerializer, UnitSerializer, LoanSerializer
from .models import Building, Unit, Loan

class BuildingCreateView(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    #queryset = Building.objects.all()
    serializer_class = BuildingSerializer

    def get_queryset(self):
    	return Building.objects.all()

    def perform_create(self, serializer):
        """Save the post data when creating a new building."""
        serializer.save()
        
class BuildingDetailsView(generics.RetrieveUpdateDestroyAPIView):
    """This class handles the http GET, PUT and DELETE requests."""

    queryset = Building.objects.all()
    serializer_class = LoanSerializer

    def get_object(self):
        queryset = self.get_queryset()
        building = get_object_or_404(queryset, **self.kwargs)
        units = building.unit_set.all()

        # create loan for the building
        loan = Loan.objects.get_or_create(building_id=building)[0]
        loan.save()

        return loan

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
