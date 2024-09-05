from django.contrib import admin
from .models import Cart, Products, CartProducts

# Register your models here.

class ProductsInline(admin.TabularInline):
    model = CartProducts


class CartAdmin(admin.ModelAdmin):
    fields = ['salesman', 'customer', 'completed']
    inlines = [ProductsInline]

admin.site.register(Cart, CartAdmin)
