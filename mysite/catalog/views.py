from django.shortcuts import render
from .models import *

def get_goods(request):
    products = Product.objects.all()
    categories = Category.objects.all()
    return render(request, 'catalog\goods.html', {'products': products, 'categories': categories})#,models.Goods.text, models.Goods.description, models.Goods.price
