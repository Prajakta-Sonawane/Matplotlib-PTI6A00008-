from django.shortcuts import render
from .models import Sales
import matplotlib.pyplot as plt
from .utils import get_plot,Histogram,bargraph
# Create your views here.

def button_view(request):
    return render(request, "sales/button.html")

def main_view(request):
    qs = Sales.objects.all()
    x = [x.item for x in qs]
    y = [y.price for y in qs]
    chart = get_plot(x,y)
    return render(request, 'sales/main.html', {'chart': chart})
def hist_view(request):
    qs = Sales.objects.all()
    x = [x.item for x in qs]  
    chart = Histogram(x)
    return render(request, 'sales/main.html',{'chart':chart})
def bar_view(request):
    qs = Sales.objects.all()
    x = [x.item for x in qs]
    y = [y.price for y  in qs]    
    chart = bargraph(x,y)
    return render(request, 'sales/main.html',{'chart':chart})    