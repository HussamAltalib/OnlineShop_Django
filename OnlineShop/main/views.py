from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from store.models import Product

# Create your views here.

def homepage(request : HttpRequest):
   products = Product.objects.all().filter(is_available=True)

   context = {
      'products': products,
   }

   return  render(request, "main/homepage.html", context)