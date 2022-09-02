import math

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponseNotFound

from account.models import User
from cart.models import Order, ProductsInOrder
from catalog.models import Product
from django.core.mail import send_mail, BadHeaderError
from appleshop.settings import RECIPIENTS_EMAIL, DEFAULT_FROM_EMAIL


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
    user = request.user
    context = {
        'next': path,
    }

    cart = request.session.get('cart', None)

    if cart:
        products = {}
        product_list = Product.objects.filter(pk__in=cart.keys()).values('id', 'title', 'description','image_url','price')

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
        context['first_name'] = user.first_name
        context['last_name'] = user.last_name
        context['phone'] = user.phone
        address = f"г.{user.city}, ул.{user.street}, д.{user.house}, кв.{user.flat}"

        context['address'] = address

    return render(request, 'cart.html', context)


@login_required(login_url='login')
def view_order(request):
    if request.method == 'POST':
        user_id = request.user.pk
        user = User.objects.get(pk=user_id)

        cart = request.session['cart']

        if len(cart) > 0:
            order = Order.objects.create(customer=user)


            order.paymentmethod = request.POST.get("type2")
            order.deliverytype = request.POST.get("type1")
            order.dateofdelivery = request.POST.get("dateofdelivery")
            order.address = f"г.{user.city}, ул.{user.street}, д.{user.house}, кв.{user.flat}"
            order.phone = user.phone



            for key, value in cart.items():
                product = Product.objects.get(pk=key)
                quantity = value['quantity']
                ProductsInOrder.objects.create(order=order, product=product, quantity=quantity)

            total_price = []
            products = {}
            product_list = Product.objects.filter(pk__in=cart.keys()).values('id', 'title', 'description', 'image_url','price')

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
            message = f' Ваш заказ № {order.id}\n Дата заказа: {order.created},\n Общая стоимость: {order.total_price}\n Дата доставки: {order.dateofdelivery}'
            send_mail(f'от AppleStore', message,
                      DEFAULT_FROM_EMAIL, RECIPIENTS_EMAIL)

    return render(request,'order_success.html', context={'order': order})

def delete_all(request):
    if request.method == 'POST':
        request.session['cart'] = {}
        request.session.modified = True
        return render(request,'cart_success.html')






