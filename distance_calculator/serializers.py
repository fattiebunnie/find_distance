from rest_framework import serializers
from distance_calculator.models import Calculator


class CalculatorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Calculator
        # fields = ['id', 'title', 'code', 'linenos', 'language', 'style']
        fields = ['id', 'longitude01', 'latitude01', 'longitude02', 'latitude02']