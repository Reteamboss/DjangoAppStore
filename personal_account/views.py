from django.shortcuts import render
from account.models import User
from cart.models import Order, ProductsInOrder
from catalog.models import Product

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
    return render(request, 'personal_account2.html', context)

def personal_account_index(request):
    return render(request, 'personal_account.html')



