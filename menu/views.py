from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from menu.models import ProductList

class HomeView(TemplateView):
    template_name = 'index.html'


class ProductDetailView(TemplateView):
    template_name = 'product-inner.html'


class ProductListView(TemplateView):
    template_name = 'product.html'

class RecipesView(TemplateView):
    template_name = 'recipes.html'