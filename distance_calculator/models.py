from django.db import models
# from django.contrib.auth.models import User
# from distance_calculator.views import CalculatorView




class Calculator(models.Model):
    
    longitude01 = models.CharField(max_length=4)
    latitude01  = models.CharField(max_length=4)
    longitude02 = models.CharField(max_length=4)
    latitude02  = models.CharField(max_length=4)

    
    # distance = models.CharField(max_length=20)

    # print("PRIMARY HEY HERE*********************************************************************************************")
    # print(latitude01)

    # @property
    # def calc_dist(self):
    #     if self.latitude01 is None:
    #         self. = self.goals * 4
    #     return self._total_points

    # distance  = models.FloatField(max_length=50)

    # user = models.ForeignKey(
    #     User,
    #     on_delete=models.CASCADE,
    #     )
    # longitude01 = CalculatorView.calculator.longitude01
    # latitude01  = CalculatorView.calculator.latitude01
    # longitude02 = CalculatorView.calculator.longitude02
    # latitude02  = CalculatorView.calculator.latitude02

    # earthradius = models.IntegerField(default = EARTH_RADIUS)
    # distance = models.FloatField()
    # distance = models.FloatField(default = 2 * earthradius 
    #     * math.asin( math.sqrt(
    #     ( math.sin(( latitude02 - latitude01) / 2) ** 2) 
    #     + math.cos( latitude01) * math.cos( latitude02) 
    #     * math.sin(( longitude02 - longitude01) / 2))))
    # def save(self, *args, **kwargs):
    #     self.calc_distance()
    #     super().save(*args, **kwargs)

    # def calc_distance(self, longitude01, latitude01, longitude02, latitude02):
    #     if (is_number(self.cleaned_data['longitude01']) 
    #         and is_number(self.cleaned_data['longitude02']) 
    #         and is_number(self.cleaned_data['latitude01']) 
    #         and is_number(self.cleaned_data['latitude02'])):

    #         longitude01 = math.radians(float(longitude01))
    #         latitude01  = math.radians(float(latitude01))
    #         longitude02 = math.radians(float(longitude02))
    #         latitude02  = math.radians(float(latitude02))

    #         EARTH_RADIUS = 6378137

    #         distance = (2 * EARTH_RADIUS 
    #         * math.asin( math.sqrt(
    #         ( math.sin(
    #             ( math.radians(float(latitude02)) - math.radians(float(latitude01)) ) / 2
    #             ) ** 2 ) 
    #         + (math.cos( math.radians(float(latitude01)) ) 
    #         * math.cos( math.radians(float(latitude02)) ) 
    #         * (math.sin(( math.radians(float(longitude02)) - math.radians(float(longitude01)) ) / 2))**2
    #         ))))
    #         return distance
    #     else:
    #         return "Input is not an integer or a float!"


    # class Meta:
    #     ordering = ['created']


# class Calculator(models.Model):
#     # created = models.DateTimeField(auto_now_add=True)
#     # title = models.CharField(max_length=100, blank=True, default='')
#     # # print(dir(latitude01))
#     # linenos = models.BooleanField(default=False)
#     # language = models.CharField(choices=LANGUAGE_CHOICES, default='python', max_length=100)
#     # style = models.CharField(choices=STYLE_CHOICES, default='friendly', max_length=100)

#     # longitude01 = models.CharField(default=request.POST['longitude01'])
#     # latitude01  = models.CharField(default=request.POST['latitude01'])
#     # longitude02 = models.CharField(default=request.POST['longitude02'])
#     # latitude02  = models.CharField(default=request.POST['latitude02'])

#     longitude01 = models.CharField(CalculatorView.calculator.longitude01)
#     latitude01  = models.CharField(CalculatorView.calculator.latitude01)
#     longitude02 = models.CharField(CalculatorView.calculator.longitude02)
#     latitude02  = models.CharField(CalculatorView.calculator.latitude02)

#     # longitude01 = CalculatorView.calculator.longitude01
#     # latitude01  = CalculatorView.calculator.latitude01
#     # longitude02 = CalculatorView.calculator.longitude02
#     # latitude02  = CalculatorView.calculator.latitude02

#     # earthradius = models.IntegerField(default = EARTH_RADIUS)
#     # distance = models.FloatField()
#     distance = models.FloatField(default = 2 * earthradius 
#         * math.asin( math.sqrt(
#         ( math.sin(( latitude02 - latitude01) / 2) ** 2) 
#         + math.cos( latitude01) * math.cos( latitude02) 
#         * math.sin(( longitude02 - longitude01) / 2))))


#     class Meta:
#         ordering = ['created']

