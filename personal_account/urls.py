from django.urls import path
from .views import personal_account_orders_view,personal_info,add_info
from django.conf.urls import url




urlpatterns = [

    path('personal_info/', personal_info, name='personal_info'),
    path('add_info/', add_info, name='add_info'),
    path('', personal_account_orders_view, name='personal_account_orders'),


]
