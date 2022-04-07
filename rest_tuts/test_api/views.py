from django.shortcuts import render
from . models import Booked, Shows
from rest_framework import viewsets
from .serializers import showsSerializer, bookedSerializer



class ShowViewset(viewsets.ModelViewSet):
    queryset = Shows.objects.all()
    serializer_class = showsSerializer


class BookedViewset(viewsets.ModelViewSet):
    queryset = Booked.objects.all()
    serializer_class = bookedSerializer



