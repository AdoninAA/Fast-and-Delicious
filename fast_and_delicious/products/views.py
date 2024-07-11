from django.shortcuts import render
from django.views import View
from django.views.generic import DetailView

from .models import Product, Category
class IndexView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'base/base.html')

class ProductsDetailView(DetailView):
    model = Product
    pk_url_kwarg = 'product_id'
    template_name = 'products/product_detail.html'

class CategoryDetailView(DetailView):
    model = Category
    pk_url_kwarg = 'category_id'
    template_name = 'products/category_detail.html'