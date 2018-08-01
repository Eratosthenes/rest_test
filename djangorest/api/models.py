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
