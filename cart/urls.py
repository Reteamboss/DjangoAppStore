from django.urls import path

from cart import views

app_name = 'cart'

urlpatterns = [
    path('order/', views.view_order, name='order'),
    path('add/', views.add_to_cart, name='add_to_cart',),
    path('delete_all/', views.delete_all, name='delete_all',),
    path('', views.view_cart, name='cart',),
]