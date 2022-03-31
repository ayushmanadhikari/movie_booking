from django.shortcuts import render
from . models import Shows
from rest_framework import viewsets
from .serializers import showsSerializer




class showsViewset(viewsets.ModelViewSet):
    query = Shows.objects.all()
    serializer_class = showsSerializer
