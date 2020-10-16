from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from .serializers import TempSerializer
from .models import Temp


class TempViewSet(viewsets.ModelViewSet):
    queryset = Temp.objects.all().order_by('created_at')
    serializer_class = TempSerializer