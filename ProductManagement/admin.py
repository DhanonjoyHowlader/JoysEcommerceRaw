from django.contrib import admin
from .models import Product, Cart, Order, Review,Slider

# Register your models here.
admin.site.register([Product, Cart, Order, Review,Slider])