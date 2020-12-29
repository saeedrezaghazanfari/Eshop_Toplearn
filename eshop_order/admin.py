from django.contrib import admin
from .models import OrderDetail, Order
# Register your models here.

admin.site.register(Order)
admin.site.register(OrderDetail)