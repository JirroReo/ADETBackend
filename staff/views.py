from django.shortcuts import render
from rest_framework import viewsets

from .serializers import StaffSerializer, RoleSerializer
from .models import Staff, Role

# Create your views here.

class StaffAPIView(viewsets.ModelViewSet):
    queryset = Staff.objects.all().order_by('staff_id')
    serializer_class = StaffSerializer

class RoleAPIView(viewsets.ModelViewSet):
    queryset = Role.objects.all().order_by('role_id')
    serializer_class = RoleSerializer