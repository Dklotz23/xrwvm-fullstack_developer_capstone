
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.
class CarMake(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name


class CarModel(models.Model):
    car_make = models.ForeignKey(CarMake, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    CAR_TYPES = [
        ('SEDAN', 'Sedan'),
        ('SUV', 'SUV'),
        ('WAGON', 'Wagon'),
        ('COUP', 'Coup'),
        ('PICKUP', 'Pickup'),
        ('HATCHBACK', 'Hatchback'),
        ('VAN', 'Van'),
        ('JEEP', 'Jeep')
    ]
    type = models.CharField(max_length=10, choices=CAR_TYPES, default='SUV')
    year = models.IntegerField(default=2026,
                               validators=[
                                   MaxValueValidator(2026),
                                   MinValueValidator(2010)
                                ])

    def __str__(self):
        return self.name
        