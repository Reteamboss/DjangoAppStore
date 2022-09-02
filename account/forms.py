from django import forms

from account.models import User


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Password', required=True)
    password2 = forms.CharField(label='Repeat password', required=True)
    first_name = forms.CharField(label='Ваше имя', required=True)
    last_name = forms.CharField(label='Ваша фамилия', required=True)
    phone = forms.CharField(label='Номер телефона', required=True, help_text='+799999999999')
    city = forms.CharField(label='Город', required=True)
    street = forms.CharField(label='Улица', required=True)
    house = forms.CharField(label='Дом', required=True)
    flat = forms.CharField(label='№ квартиры', required=True)

    class Meta:
        model = User
        fields = ('email', )

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Пароли не совпадают.')
        return cd['password2']


