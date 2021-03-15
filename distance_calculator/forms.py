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


"""
from django import forms
from distance_calculator.models import Calculator


def is_number(s):
        try:
            float(s)
            return True
        except ValueError:
            return False

# def calc_distance(longitude01, latitude01, longitude02, latitude02):
#     if is_number(longitude01) and is_number(longitude02) and is_number(latitude01) and is_number(latitude02):
#         longitude01 = math.radians(float(longitude01))
#         latitude01  = math.radians(float(latitude01))
#         longitude02 = math.radians(float(longitude02))
#         latitude02  = math.radians(float(latitude02))

#         EARTH_RADIUS = 6378137

#         distance = (2 * EARTH_RADIUS 
#         * math.asin( math.sqrt(
#         ( math.sin(
#             ( latitude02 - latitude01 ) / 2
#             ) ** 2 ) 
#         + (math.cos( latitude01 ) 
#         * math.cos( latitude02 ) 
#         * (math.sin(( longitude02 - longitude01 ) / 2))**2
#         ))))
#         return distance
#     else:
#         return "Input is not an integer or a float!"




class CalcForm(forms.ModelForm):
    def calc_distance(self, longitude01, latitude01, longitude02, latitude02):
        if (is_number(self.cleaned_data['longitude01']) 
            and is_number(self.cleaned_data['longitude02']) 
            and is_number(self.cleaned_data['latitude01']) 
            and is_number(self.cleaned_data['latitude02'])):

            longitude01 = math.radians(float(longitude01))
            latitude01  = math.radians(float(latitude01))
            longitude02 = math.radians(float(longitude02))
            latitude02  = math.radians(float(latitude02))

            EARTH_RADIUS = 6378137

            distance = (2 * EARTH_RADIUS 
            * math.asin( math.sqrt(
            ( math.sin(
                ( latitude02 - latitude01 ) / 2
                ) ** 2 ) 
            + (math.cos( latitude01 ) 
            * math.cos( latitude02 ) 
            * (math.sin(( longitude02 - longitude01 ) / 2))**2
            ))))
            return distance
        else:
            return "Input is not an integer or a float!"


    longitude01 = forms.CharField(label='longitude01', max_length=100)
    latitude01 = forms.CharField(label='latitude01', max_length=100)
    longitude02 = forms.CharField(label='longitude02', max_length=100)
    latitude02 = forms.CharField(label='latitude02', max_length=100)
    
    EARTH_RADIUS = 6378137
    
    longitude_01 = cleaned_data['longitude01']
    latitude_01  = cleaned_data['latitude01']
    longitude_02 = cleaned_data['longitude02']
    latitude_02  = cleaned_data['latitude01']


    if (is_number(longitude_01) 
        and is_number(longitude_02) 
        and is_number(latitude_01) 
        and is_number(latitude_02)):

        longitude_01 = math.radians(float(longitude_01))
        latitude_01  = math.radians(float(latitude_01))
        longitude_02 = math.radians(float(longitude_02))
        latitude_02  = math.radians(float(latitude_02))

        EARTH_RADIUS = 6378137

        distance = (2 * EARTH_RADIUS 
        * math.asin( math.sqrt(
        ( math.sin(
            ( latitude02 - latitude01 ) / 2
            ) ** 2 ) 
        + (math.cos( latitude01 ) 
        * math.cos( latitude02 ) 
        * (math.sin(( longitude02 - longitude01 ) / 2))**2
        ))))


    # distance = (2 * EARTH_RADIUS 
    #         * math.asin( math.sqrt(
    #         ( math.sin(
    #             ( cleaned_data['latitude02'] - cleaned_data['latitude01'] ) / 2
    #             ) ** 2 ) 
    #         + (math.cos( cleaned_data['latitude01'] ) 
    #         * math.cos( cleaned_data['latitude02'] ) 
    #         * (math.sin(( cleaned_data['longitude02'] - cleaned_data['longitude01'] ) / 2))**2
    #         )))) if (is_number(cleaned_data['longitude01']) 
    #         and is_number(cleaned_data['longitude02']) 
    #         and is_number(cleaned_data['latitude01']) 
    #         and is_number(cleaned_data['latitude02'])) else ""

        

    
    # distance = calc_distance(self, longitude01, latitude01, longitude02, latitude02)
    # distance = calc_distance(self.cleaned_data['longitude01'], 
    #     self.cleaned_data['latitude01'], 
    #     self.cleaned_data['longitude02'], 
    #     self.cleaned_data['latitude02'])    
    class Meta:
        model = Calculator
        fields = ['id', 'longitude01', 'latitude01', 'longitude02', 'latitude02', 'distance']

"""