from rest_framework import serializers

from reactdjango.models import Car


class CarSer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = '__all__'