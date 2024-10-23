from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView
# Create your views here.

class HomeView(TemplateView):
	template_name = 'index.html'

class ProductListView(TemplateView):
	template_name = 'product.html'
	def get_context_data(self, **kwargs):
		context = {
            'product': Product.objects.all(),
        }
		return context

