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
    try:
        whole_total = Cart.objects.aggregate(Sum('price'))
        whole_weight = Cart.objects.aggregate(Sum('quantityInGrams'))
        total = (whole_total['price__sum'])
        weight = (whole_weight['quantityInGrams__sum'])
        if weight > 501:
            pandp = 2.50
            final_total = (pandp+total)
            return render(request, 'cart_detail.html', {'whole_cart': whole_cart, 'total': total, 'weight': weight, 'pandp': pandp, 'final_total':final_total})
        elif weight > 251 and weight < 500:
            pandp = 2.00
            final_total = (pandp+total)
            return render(request, 'cart_detail.html', {'whole_cart': whole_cart, 'total': total, 'weight': weight, 'pandp': pandp, 'final_total':final_total})
        elif weight > 40 and weight < 250:
            pandp = 1.50
            final_total = (pandp+total)
            return render(request, 'cart_detail.html', {'whole_cart': whole_cart, 'total': total, 'weight': weight, 'pandp': pandp, 'final_total':final_total})
    except:
        return render(request, 'cart_detail.html', {'error': 'no items in your cart'})
    return render(request, 'cart_detail.html', {'whole_cart': whole_cart, 'error': 'minimum weight not met'})


def delete_item(request, id):
     item = Cart.objects.get(id=id)
     item.delete()
     return HttpResponseRedirect(reverse('cart_detail'))