from django.shortcuts import render
from . models import Shows
from rest_framework import viewsets
from .serializers import showsSerializer, UserSerializer
from django.contrib.auth.models import User



class ShowViewset(viewsets.ModelViewSet):
    queryset = Shows.objects.all()
    serializer_class = showsSerializer


class userViewset(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

