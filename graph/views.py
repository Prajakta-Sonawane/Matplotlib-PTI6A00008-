from django.shortcuts import render
from .models import Sales
from .utils import get_plot,Histogram,bargraph,Scatter
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
    y = [y.item for y in qs]  
    chart = Histogram(y)
    return render(request, 'sales/main.html',{'chart':chart})

def bar_view(request):
    qs = Sales.objects.all()
    x = [x.item for x in qs]
    y = [y.price for y  in qs]    
    chart = bargraph(x,y)
    return render(request, 'sales/main.html',{'chart':chart})

def scatter_view(request):
    qs = Sales.objects.all()
    x = [x.item for x in qs]
    y = [y.price for y  in qs]    
    chart = Scatter(x,y)
    return render(request, 'sales/main.html',{'chart':chart})      

    