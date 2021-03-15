from django.shortcuts import render, redirect
from rest_framework import viewsets

from django.views.generic import TemplateView

from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

from distance_calculator.serializers import CalculatorSerializer
from distance_calculator.forms import CalcForm
from distance_calculator.models import Calculator
import math

class CalculatorView(TemplateView):
    template_name = 'public/input.html'

    def index(request):
        return render(request, "input.html")

    def get(self, request):
        form = CalcForm()
        return render(request, self.template_name, {'form': form})

    
    def calculator (request):

        form = CalcForm(request.POST)
        if form.is_valid():
            # save into db
            calculator = form.save(commit= False)
            calculator.save()
            longitude01 = form.cleaned_data['longitude01']
            latitude01  = form.cleaned_data['latitude01']
            longitude02 = form.cleaned_data['longitude02']
            latitude02  = form.cleaned_data['latitude02']
            
            # distance = form.cleaned_data['distance']
            distance = calc_distance(longitude01, latitude01, longitude02, latitude02)

            form = CalcForm()
            return render(request, "result.html", {"result": distance})
        else:
            error_message = "invalid input"
            return render(request, "result.html", {"result": error_message})


@csrf_exempt
def calculator_list(request):
    """
    List all code calculator, or create a new calculator.
    """
    if request.method == 'GET':
        calculator = Calculator.objects.all()
        serializer = CalculatorSerializer(calculator, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = CalculatorSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def calculator_detail(request, pk):
    """
    Retrieve, update or delete a code calculator.
    """
    try:
        calculator = Calculator.objects.get(pk=pk)
    except Calculator.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = CalculatorSerializer(calculator)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = CalculatorSerializer(calculator, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        calculator.delete()
        return HttpResponse(status=204)



def calc_distance(longitude01, latitude01, longitude02, latitude02):
    if is_number(longitude01) and is_number(longitude02) and is_number(latitude01) and is_number(latitude02):
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


def is_number(s):
        try:
            float(s)
            return True
        except ValueError:
            return False