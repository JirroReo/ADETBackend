"""adetbackend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from categories.views import CategoryAPIView
from products.views import ProductAPIView
from supplier.views import SupplierAPIView
from orders.views import OrderAPIView
from customers.views import CustomerAPIView
from staff.views import StaffAPIView, RoleAPIView

router = routers.DefaultRouter()
router.register(r'categorys', CategoryAPIView)
router.register(r'products', ProductAPIView)
router.register(r'suppliers', SupplierAPIView)
router.register(r'orders', OrderAPIView)
router.register(r'customers', CustomerAPIView)
router.register(r'staffs', StaffAPIView)
router.register(r'roles', RoleAPIView)



urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls)),
]
