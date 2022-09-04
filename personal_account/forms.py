from django import forms


class CustomerInfo(forms.Form):
    first_name = forms.CharField(label='Ваше имя', required=True)
    last_name = forms.CharField(label='Ваша фамилия', required=True)
    phone = forms.CharField(label='Номер телефона', required=True, help_text='+799999999999')
    city = forms.CharField(label='Город', required=True)
    street = forms.CharField(label='Улица', required=True)
    house = forms.CharField(label='Дом', required=True)
    flat = forms.CharField(label='Квартира', required=True)