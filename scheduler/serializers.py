from rest_framework import serializers
from models import Reservations


class EmployeesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservations
        fields = '__all__'
