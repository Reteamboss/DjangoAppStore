from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from account.models import User
from cart.models import Order, ProductsInOrder
from catalog.models import Product
from .forms import CustomerInfo
from django.http import HttpResponseRedirect

@login_required(login_url='/accounts/login/')
def personal_account_orders_view(request):


    context = {}
    user_id = request.user.pk
    order_dict = Order.objects.filter(customer=user_id).values('id','dateofdelivery','created','products','total_price')


    context['order_list'] = order_dict
    prodlist = []
    for order in order_dict:
        prod = Product.objects.get(pk=order['products'])
        prodlist.append(prod)
    context['user_id'] = user_id
    # context['prodlist'] = prodlist
    return render(request, 'personal_orders.html', context)

@login_required(login_url='/accounts/login/')
def personal_info(request):
    context = {}
    user = request.user
    context['user'] = user
    return render(request, 'personal_info.html',context=context)

@login_required(login_url='/accounts/login/')
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







