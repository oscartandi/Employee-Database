from rest_framework import viewsets
from . import models
from . import serializers

class EmployeeViewset(viewsets.ModelViewSet):
   serializer_class= serializers.EmployeeSerializer
   queryset = models.Employee.objects.all()


# List(), Retrive(), Create(), Update()
#     
