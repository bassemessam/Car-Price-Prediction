from django.db import models


class Prediction(models.Model):
    """docstring for prediction."""

    name = 'prediction'
    year = models.IntegerField()
    # Present_Price = models.DecimalField(decimal_places=2,max_digits=5)
    # Kms_Driven = models.IntegerField()
    # Owner = models.IntegerField()
    # Fuel_Type_Petrol = models.CharField(max_length=20)
    # Seller_Type_Individual = models.CharField(max_length=20)
    # Transmission_Manual = models.CharField(max_length=20)
    # def __str__(self):
    #     return self.year


# Create your models here.
