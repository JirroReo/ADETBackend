from django.db.models import fields
from rest_framework import serializers
from .models import Staff, Role

from django.contrib.auth.hashers import make_password

class StaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = Staff
        fields = ('staff_id', 'first_name', 'last_name', 'address', 'phone', 'email')
        depth=3

class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = '__all__'
        depth=3