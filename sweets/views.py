from django.shortcuts import render
from .models import Sweets, Cart
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import CartForm
from decimal import Decimal
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.db.models import Sum


def index(request):
    sweets = Sweets.objects.all()
    return render (request, 'home.html', {'sweets': sweets, 'form': CartForm})

def cart_add(request, id):
    product = Sweets.objects.get(id=id)
    if request.method == 'POST': #method is post as we are inputting data
        form = CartForm(request.POST) #creating an instance for this form
        newItem = form.save(commit=False)
        newItem.name = product.name
        newItem.weightPerSweet = product.weight
        newItem.price = product.price*(int(request.POST['quantityInGrams'])) #price of product per gram times by quantity
        newItem.save()
        return HttpResponseRedirect(reverse('index'))
    return HttpResponseRedirect(reverse('index'))

def cart_detail(request):
    whole_cart = Cart.objects.all()
    whole_total = Cart.objects.aggregate(Sum('price'))
    total = (whole_total['price__sum'])
        #return render(request, 'cart_detail.html', {'whole_cart': whole_cart}, whole_total)
    return render(request, 'cart_detail.html', {'whole_cart': whole_cart, 'total': total})