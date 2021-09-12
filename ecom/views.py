from django.shortcuts import render, redirect 
from django.http import JsonResponse
import json
import datetime
from .models import * 
from .utils import *
from .forms import *

def store(request):
    data = cartData(request)
    cartItems = data['cartItems']
    order = data['order']
    items = data['items']
    products = Product.objects.all()
    sliders = Company_slider.objects.all()
    context = {'products':products, 'cartItems':cartItems,'sliders':sliders}
    return render(request, 'store.html', context)


def cart(request):
    data = cartData(request)

    cartItems = data['cartItems']
    order = data['order']
    items = data['items']

    context = {'items':items, 'order':order, 'cartItems':cartItems}
    return render(request, 'cart.html', context)

def chekout(request):
    data = cartData(request)
    
    cartItems = data['cartItems']
    order = data['order']
    items = data['items']

    context = {'items':items, 'order':order, 'cartItems':cartItems}
    return render(request, 'chekout.html', context)

def updateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']
    print('Action:', action)
    print('Product:', productId)

    customer = request.user.customer
    product = Product.objects.get(id=productId)
    order, created = Order.objects.get_or_create(customer=customer, complete=False)

    orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)

    if action == 'add':
        orderItem.quantity = (orderItem.quantity + 1)
    elif action == 'remove':
        orderItem.quantity = (orderItem.quantity - 1)

    orderItem.save()

    if orderItem.quantity <= 0:
        orderItem.delete()


    
    return JsonResponse('Item was added', safe=False)

def processOrder(request):
    transaction_id = datetime.datetime.now().timestamp()
    data = json.loads(request.body)

    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
    else:
        customer, order = guestOrder(request, data)

    total = float(data['form']['total'])
    order.transaction_id = transaction_id

    if total == order.get_cart_total:
        order.complete = True
    order.save()

    if order.shipping == True:
        ShippingAddress.objects.create(
        customer=customer,
        order=order,
        address=data['shipping']['address'],
        city=data['shipping']['city'],
        state=data['shipping']['state'],
        zipcode=data['shipping']['zipcode'],
        country=data['shipping']['country'],
        phone=data['shipping']['phone'],
        livraison=data['shipping']['livraison'],
        )
    if order.shipping == True:
        Information.objects.create(
        customer=customer,
        order=order,
        address=data['shipping']['address'],
        city=data['shipping']['city'],
        state=data['shipping']['state'],
        zipcode=data['shipping']['zipcode'],
        country=data['shipping']['country'],
        phone=data['shipping']['phone'],
        livraison=data['shipping']['livraison'],
        suggestion=data['shipping']['suggestion'],
        )

    return JsonResponse('Payment submitted..', safe=False)

def view(request,pk):
    data = cartData(request)

    cartItems = data['cartItems']
    order = data['order']
    items = data['items']

    product = Product.objects.get(id=pk)
    context = {'product':product, 'cartItems':cartItems}
    return render(request, 'view.html', context)
def map(request):
    data = cartData(request)

    cartItems = data['cartItems']
    order = data['order']
    items = data['items']

    products = Product.objects.all()

    context = {'products':products, 'cartItems':cartItems}
    return render(request, 'map.html', context)
def contact(request):
    data = cartData(request)

    cartItems = data['cartItems']
    order = data['order']
    items = data['items']
    products = Product.objects.all()
    form = ContactForm()

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('store')
            
    context = {'form':form,'products':products, 'cartItems':cartItems}
    return render(request, 'contactus.html', context)
def thanks(request):
    context = {} 
    return render(request,'thanks.html',)
