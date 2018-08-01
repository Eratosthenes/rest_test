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

    def get_treasury_rate(self):
    	return 3.0

    # returns constant, because calculation for Loan Proceeds was not defined in assignment
    def calculate_loan_proceeds(self):
    	return 10

    def loan_term(self):
    	return 10 

    def calculate_payoff_amount(self):
    	return 1.23

    def get_object(self):
        queryset = self.get_queryset()
        building = get_object_or_404(queryset, **self.kwargs)
        units = building.unit_set.all()

        # create loan for the building
        loan = Loan.objects.get_or_create(building_id=building)[0]

        # calculate total annual rent for building
        total_annual_rent = sum([unit.monthly_rent * 12 for unit in units])
        expenses = building.marketing + building.taxes + building.insurance \
                    + building.repairs + building.administration + building.payroll \
                    + building.utility + building.management

        net_operating_income = total_annual_rent - expenses
        loan.debt_rate = (self.get_treasury_rate() + 0.2) / 100

        debt_repayment = loan.debt_rate * self.calculate_loan_proceeds()
        debt_service = net_operating_income / debt_repayment
        value = net_operating_income / building.capitalization_rate if building.capitalization_rate != 0 else net_operating_income
        present_value = self.calculate_payoff_amount() / (1 + loan.debt_rate) ** (12 * self.loan_term())

        loan.loan_amount = min(value, present_value) if debt_service >= 1.25 else value
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
