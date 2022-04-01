from rest_framework import serializers
from . models import Shows, movie, Booked
from django.contrib.auth.models import User


class showsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shows
        fields = ('s_id', 'm_id', 'price', 'capacity')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


