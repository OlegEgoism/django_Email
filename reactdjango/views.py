from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from rest_framework.response import Response

from reactdjango.models import Car
from reactdjango.serializers import CarSer


class CarViewSet(viewsets.ViewSet):
    def list(self, request):
        cars=Car.objects.all()
        ser = CarSer(cars, many=True)
        return Response(ser.data)


    def retrieve(self, request, pk=None):
        pass

