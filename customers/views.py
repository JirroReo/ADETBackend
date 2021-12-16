from django.shortcuts import render
from rest_framework import viewsets

from .serializers import CustomerSerializer
from .models import Customer

# Create your views here.

class CustomerAPIView(viewsets.ModelViewSet):
    queryset = Customer.objects.all().order_by('customer_id')
    serializer_class = CustomerSerializer