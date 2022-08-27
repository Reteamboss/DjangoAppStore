from django.urls import path
from .views import personal_account_orders_view,personal_account_index
from django.conf.urls import url




urlpatterns = [

    path('orders/', personal_account_orders_view, name='personal_account_orders'),
    path('', personal_account_index, name='personal_account_index'),


]
