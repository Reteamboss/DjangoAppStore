from django.urls import path
from .views import personal_account_orders_view,personal_info,change_info
from django.conf.urls import url




urlpatterns = [

    path('personal_info/', personal_info, name='personal_info'),
    path('change_info/', change_info, name='change_info'),
    path('', personal_account_orders_view, name='personal_account_orders'),


]
