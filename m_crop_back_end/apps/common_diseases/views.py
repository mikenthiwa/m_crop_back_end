from django.shortcuts import render
from rest_framework import viewsets
from .serializers import CommonDiseaseSerializer
from .models import CommonDisease


class CommonDiseasesViewSet(viewsets.ModelViewSet):
    queryset = CommonDisease.objects.all()
    serializer_class = CommonDiseaseSerializer


