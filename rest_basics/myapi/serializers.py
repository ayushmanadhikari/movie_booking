from attr import field
from .models import Hero
from rest_framework import serializers


class HeroSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Hero
        field = ('name', 'alias')