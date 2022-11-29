from django.http import HttpRequest
from django.shortcuts import redirect, render
from app.models import Order
from app.forms import ProductForm

def index(request):
    assert isinstance(request, HttpRequest)
    orders = Order.objects.all()
    return render(
        request,
        'app/orders/index.html',
        {
            'orders': orders
        }
    )
    
def create(request):
    form = OrderForm()
    return render(
        request, 
        'app/orders/create.html',
        {
            'form': form
        }
    )
    
def save(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/orders')
    
def edit(request, id):
    assert isinstance(request, HttpRequest)
    if request.method == "GET":
        if id == 0:
            form = OrderForm()
        else:
            Order = Order.objects.get(pk=id)
            form = OrderForm(instance=Order)
        return render(
            request,
            'app/orders/edit.html',
            {
                'form': form
            }
        )
    else:
        if id == 0:
            form = OrderForm(request.POST)
        else:
            Order = Order.objects.get(pk=id)
            form = OrderForm(request.POST, instance=Order)
        if form.is_valid():
            form.save()
        return redirect('/orders')
    
def delete(request, id):
    Order = Order.objects.get(pk=id)
    Order.delete()
    return redirect('/orders')