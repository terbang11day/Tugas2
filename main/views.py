from django.shortcuts import render
from .models import Product

def show_main(request):
    benda = Product.objects.all
    context = {
        'benda' : benda
    }

    return render(request, "main.html", context)