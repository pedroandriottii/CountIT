from django.contrib import admin
from .models import Category, Product

@admin.register(Category)
class categoryAdmin(admin.ModelAdmin):
    ...

@admin.register(Product)
class productAdmin(admin.ModelAdmin):
    ...