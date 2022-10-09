from dataclasses import field, fields
from re import template
from sre_constants import SUCCESS
from unicodedata import category
from django.shortcuts import render
from .models import Category,Product
from django.views.generic.edit import CreateView, UpdateView,DeleteView
from django.urls import reverse_lazy

# Create your views here.

def index(request):
    categories = Category.objects.all()
    products = Product.objects.all()
    context = {"categories":categories, "products":products}
    return render(request, "index.html", context)

def car_detail(request, car_detail):
    a = Product.objects.get(id = car_detail)
    context ={'Product' : a}
    return render(request, 'car_detail.html' , context)

def category_filter(request, category_id):
    category = Category.objects.get(id = category_id)
    categories= Category.objects.all()
    products = Product.objects.filter(category = category)
    context ={'categories' : categories, 'products':products}
    return render(request, 'index.html' , context)

class ProductCreateView(CreateView):
    model=Product
    template_name='post_new.html'
    fields=['category', 'name', 'text', 'image'] 
    success_url = '/'

    def post(self, request, *args, **kwargs):
        print(3313131)
        print(request.POST)
        return super().post(request, *args, **kwargs)

class ProductUpdateView(UpdateView):
    model=Product
    template_name='post_edit.html'
    fields=['name', 'text', 'image','tel_raqam']
    success_url = '/'

class ProductDeleteView(DeleteView):
    model=Product
    template_name='post_delete.html'
    fields=['name', 'text', 'image','tel_raqam']
    # success_url = reverse_lazy('index')
    success_url = '/'
