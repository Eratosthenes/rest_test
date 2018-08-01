from django.db import models

class Building(models.Model):
    """This class represents the building model."""
    name = models.CharField(max_length=255, blank=False, unique=True)
    address = models.CharField(max_length=255, blank=False, unique=True)
    capitalization_rate = models.FloatField(default=0.0)
    marketing = models.FloatField(default=0.0)
    taxes = models.FloatField(default=0.0)
    insurance = models.FloatField(default=0.0)
    repairs = models.FloatField(default=0.0)
    administration = models.FloatField(default=0.0)
    payroll = models.FloatField(default=0.0)
    utility = models.FloatField(default=0.0)
    management = models.FloatField(default=0.0)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        """Return a human readable representation of the model instance."""
        return "{}".format(self.name)   

class Unit(models.Model):
    building_id = models.ForeignKey(Building, on_delete=models.CASCADE)
    unit_number = models.CharField(max_length=200) # not a number since we can have unit 2A, etc
    monthly_rent = models.IntegerField(default=0)
    vacancy = models.IntegerField(default=0)
    bedrooms = models.IntegerField(default=0)
    bathrooms = models.IntegerField(default=0)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    # annual_total not included since it is just monthly_rent * 12

    def __str__(self):
    	return self.unit_number