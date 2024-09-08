from django.contrib import admin
from .models import Cart
from cart.models import CartProducts

# Register your models here.

class ProductsInline(admin.TabularInline):
    model = CartProducts

class CartAdmin(admin.ModelAdmin):
    fields = ['salesman_id', 'customer_id', 'completed']
    inlines = [ProductsInline]

admin.site.register(Cart, CartAdmin)