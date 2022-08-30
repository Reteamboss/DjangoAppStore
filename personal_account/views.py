from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from account.models import User
from cart.models import Order, ProductsInOrder
from catalog.models import Product
from .forms import CustomerInfo
from django.http import HttpResponseRedirect

def personal_account_orders_view(request):


    context = {}
    user_id = request.user.pk
    customer = User.objects.get(pk=user_id)
    order_list = Order.objects.filter(customer=customer).values('id','dateofdelivery','created','products','total_price')


    context['order_list'] = order_list
    prodlist = []
    for order in order_list:
        prod = Product.objects.get(pk=order['products'])
        prodlist.append(prod)

    context['prodlist'] = prodlist
    return render(request, 'personal_orders.html', context)

def personal_info(request):
    context = {}
    user_id = request.user.pk
    customer = User.objects.get(pk=user_id)
    context['customer'] = customer
    return render(request, 'personal_info.html',context=context)


def add_info(request):
    user_id = request.user.pk
    customer = User.objects.get(pk=user_id)
    if request.method == "POST":
        customer.first_name = request.POST.get('first_name')
        customer.last_name = request.POST.get('last_name')
        customer.phone = request.POST.get('phone')
        customer.city = request.POST.get('city')
        customer.street = request.POST.get('street')
        customer.house = request.POST.get('house')
        customer.flat = request.POST.get('flat')
        customer.save()
        return HttpResponseRedirect('/personal_info/')
    else:
        return render(request,'add_info.html',{'customer': customer})







