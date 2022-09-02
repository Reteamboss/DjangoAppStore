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
    user = request.user
    context['user'] = user
    return render(request, 'personal_info.html',context=context)


def change_info(request):
    user_id = request.user.pk
    user = User.objects.get(pk=user_id)

    customerform = CustomerInfo()
    if request.method == "POST":
        user.first_name = request.POST.get('first_name')
        user.last_name = request.POST.get('last_name')
        user.phone = request.POST.get('phone')
        user.city = request.POST.get('city')
        user.street = request.POST.get('street')
        user.house = request.POST.get('house')
        user.flat = request.POST.get('flat')
        user.save()
        return HttpResponseRedirect('/')
    else:
        return render(request,'change_info.html',{'user': user,'form':customerform})







