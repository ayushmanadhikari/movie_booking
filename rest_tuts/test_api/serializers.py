from attr import field
from rest_framework import serializers
from . models import Shows, movie, Booked
from django.contrib.auth.models import User


class showsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shows
        fields = '__all__'

class bookedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booked
        fields = '__all__'




