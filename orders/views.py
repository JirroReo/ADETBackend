from django.shortcuts import render
from rest_framework import viewsets

from .serializers import OrderSerializer
from .models import Order

# Create your views here.

class OrderAPIView(viewsets.ModelViewSet):
    queryset = Order.objects.all().order_by('order_id')
    serializer_class = OrderSerializer