from django.shortcuts import render
from .models import Sales
from .utils import get_plot
# Create your views here.

def main_view(request):
    qs = Sales.objects.all()
    x = [x.item for x in qs]
    y = [y.price for y in qs]
    chart = get_plot(x,y)
    return render(request, 'sales/main.html', {'chart': chart})