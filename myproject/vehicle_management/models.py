from django.db import models

class Vehicle(models.Model):
    VEHICLE_TYPE = (
        ('2', 'Two Wheeler'),
        ('3', 'Three Wheeler'),
        ('4', 'Four Wheeler')
    )

    vehicle_number = models.CharField(max_length=20, unique=True)
    vehicle_type = models.CharField(max_length=1, choices=VEHICLE_TYPE)
    vehicle_model = models.CharField(max_length=50)
    vehicle_description = models.TextField()

    def __str__(self):
        return self.vehicle_number

