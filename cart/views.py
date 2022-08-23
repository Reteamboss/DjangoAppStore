import math

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponseNotFound

from account.models import User
from cart.models import Order, ProductsInOrder
from catalog.models import Product


def add_to_cart(request):
    path = request.GET.get('next')

    if request.method == 'POST':
        product_id = request.GET.get('product_id')

        if 'cart' not in request.session:
            request.session['cart'] = {}

        cart = request.session.get('cart')

        if product_id in cart:
            cart[product_id]['quantity'] += 1

        else:
            cart[product_id] = {
                'quantity': 1
            }

    request.session.modified = True
    return redirect(path)


def view_cart(request):
    path = request.GET.get('next')

    context = {
        'next': path,
    }

    cart = request.session.get('cart', None)

    if cart:
        products = {}
        product_list = Product.objects.filter(pk__in=cart.keys()).values('id', 'title', 'description','image','price')

        for product in product_list:
            products[str(product['id'])] = product

        total_price = []

        for key in cart.keys():
            cart[key]['product'] = products[key]
            total_quant = cart[key]['quantity'] * int(products[key]['price'])
            total_price.append(total_quant)

        sum_total = sum(total_price)


        context['total_price'] = sum_total
        context['cart'] = cart

    return render(request, 'cart.html', context)


@login_required(login_url='login')
def view_order(request):
    if request.method == 'POST':
        user_id = request.user.pk
        customer = User.objects.get(pk=user_id)


        cart = request.session['cart']

        if len(cart) > 0:
            order = Order.objects.create(customer=customer)
            order.first_name_customer = request.POST.get("first_name")
            order.last_name_customer = request.POST.get("last_name")
            order.city = request.POST.get("city")
            order.street = request.POST.get("street")
            order.house = request.POST.get("house")
            order.flat = request.POST.get("flat")
            order.phone = request.POST.get("phone")
            order.paymentmethod = request.POST.get("type1")
            order.deliverytype = request.POST.get("type2")



            for key, value in cart.items():
                product = Product.objects.get(pk=key)
                quantity = value['quantity']
                ProductsInOrder.objects.create(order=order, product=product, quantity=quantity)

            total_price = []
            products = {}
            product_list = Product.objects.filter(pk__in=cart.keys()).values('id', 'title', 'description', 'image',
                                                                             'price')

            for product in product_list:
                products[str(product['id'])] = product


            for key in cart.keys():
                cart[key]['product'] = products[key]
                total_quant = cart[key]['quantity'] * int(products[key]['price'])
                total_price.append(total_quant)


            sum_total = sum(total_price)


            order.total_price = sum_total
            order.save()

            request.session['cart'] = {}
            request.session.modified = True

            messages.success(request, 'Заказ принят')

    return render(request,'order_success.html', context={'order': order})

def delete_product(request):
    try:
        product = Product.objects.get(id=id)
        product.delete()
        return HttpResponseRedirect('/cart/')
    except Product.DoesNotExist:
        return HttpResponseNotFound("<h2>Продукт не найден</h2>")





