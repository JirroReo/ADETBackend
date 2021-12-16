from django.contrib import admin

# Register your models here.

from .models import Staff, Role

admin.site.register(Staff)
admin.site.register(Role)
