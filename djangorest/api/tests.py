from django.test import TestCase

from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse

# Create your tests here.
from django.test import TestCase
from .models import Building

class ModelTestCase(TestCase):
    """This class defines the test suite for the building model."""

    def setUp(self):
        """Define the test client and other test variables."""
        self.building_name = "Write world class code"
        self.building = Building(name=self.building_name)

    def test_model_can_create_a_building(self):
        """Test the building model can create a building."""
        old_count = Building.objects.count()
        self.building.save()
        new_count = Building.objects.count()
        self.assertNotEqual(old_count, new_count)

# Define this after the ModelTestCase
class ViewTestCase(TestCase):
    """Test suite for the api views."""

    def setUp(self):
        """Define the test client and other test variables."""
        self.client = APIClient()
        self.building_data = {'name': 'Go to Ibiza'}
        self.response = self.client.post(
            reverse('create'),
            self.building_data,
            format="json")

    def test_api_can_create_a_building(self):
        """Test the api has bucket creation capability."""
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)        

    def test_api_can_get_a_building(self):
        """Test the api can get a given building."""
        building = Building.objects.get()
        response = self.client.get(
            reverse('details',
            kwargs={'pk': building.id}), format="json")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, building)

    def test_api_can_update_building(self):
        """Test the api can update a given building."""
        building = Building.objects.get()
        change_building = {'name': 'Something new'}
        res = self.client.put(
            reverse('details', kwargs={'pk': building.id}),
            change_building, format='json'
        )
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_api_can_delete_building(self):
        """Test the api can delete a building."""
        building = Building.objects.get()
        response = self.client.delete(
            reverse('details', kwargs={'pk': building.id}),
            format='json',
            follow=True)

        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)
