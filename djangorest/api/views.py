from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .serializers import BuildingSerializer
from .models import Building

class CreateView(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = Building.objects.all()
    serializer_class = BuildingSerializer

    def perform_create(self, serializer):
        """Save the post data when creating a new building."""
        serializer.save()
        
class DetailsView(generics.RetrieveUpdateDestroyAPIView):
    """This class handles the http GET, PUT and DELETE requests."""

    queryset = Building.objects.all()
    serializer_class = BuildingSerializer
