from rest_framework import serializers
from . models import Shows, movie, Booked


class showsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Shows
        fields = ('s_id', 'm_id', 'price', 'capacity')

