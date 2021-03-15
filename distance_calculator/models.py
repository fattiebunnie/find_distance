from django.db import models
# from django.contrib.auth.models import User
# from distance_calculator.views import CalculatorView




class Calculator(models.Model):
    
    longitude01 = models.CharField(max_length=4)
    latitude01  = models.CharField(max_length=4)
    longitude02 = models.CharField(max_length=4)
    latitude02  = models.CharField(max_length=4)

    
    