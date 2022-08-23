from django.shortcuts import render
from account.models import User
from cart.models import Order, ProductsInOrder
from catalog.models import Product

def personal_account_view(request):


    context = {}
    user_id = request.user.pk
    customer = User.objects.get(pk=user_id)
    order_list = Order.objects.filter(customer=customer).values('id','dateofdelivery','created','products','total_price')


    context['order_list'] = order_list
    pk = []
    for order in order_list:
        pk.append(order['products'])

    products = Product.objects.filter(pk__in=pk).values('title')

    context['products'] = products






    return render(request, 'personal_account.html', context)


