from django import forms
from .models import Order

class CustomerInfo(forms.Form):
    first_name_customer = forms.CharField(label='Имя получателя', required=True)
    last_name_customer = forms.CharField(label='Фамилия получателя', required=True)
    phone = forms.CharField(label='Телефон для связи', required=True, help_text='+799999999999')

class OrderCreateForm(forms.Form):

    city = forms.CharField(label='Город', required=True)
    street = forms.CharField(label='Улица', required=True)
    house = forms.CharField(label='Дом', required=True)
    flat = forms.CharField(label='Квартира', required=True)

