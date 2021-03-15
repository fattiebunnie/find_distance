from django import forms
from distance_calculator.models import Calculator
import math

class CalcForm(forms.ModelForm):
    longitude01 = forms.CharField(label='longitude01', max_length=100)
    latitude01 = forms.CharField(label='latitude01', max_length=100)
    longitude02 = forms.CharField(label='longitude02', max_length=100)
    latitude02 = forms.CharField(label='latitude02', max_length=100)
    
    class Meta:
        model = Calculator
        fields = ['id', 'longitude01', 'latitude01', 'longitude02', 'latitude02']
    # EARTH_RADIUS = 6378137
    # distance = forms.FloatField((2 * EARTH_RADIUS 
    # * math.asin( math.sqrt(
    # ( math.sin(
    #     ( math.radians(float(cleaned_data['latitude02'] )) - math.radians(float(cleaned_data['latitude01'])) ) / 2
    #     ) ** 2 ) 
    # + (math.cos( math.radians(float(latitude01)) ) 
    # * math.cos( math.radians(float(latitude02)) ) 
    # * (math.sin(( math.radians(float(longitude02)) - math.radians(float(longitude01)) ) / 2))**2
    # )))))

