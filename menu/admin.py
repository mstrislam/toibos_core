from django.contrib import admin
from menu.models import  ProductList

@admin.register(ProductList)
class ProductListAdmin(admin.ModelAdmin):
   list_display = ['title']
