from django import forms

from account.models import User


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Password', required=True)
    password2 = forms.CharField(label='Repeat password', required=True)


    class Meta:
        model = User
        fields = ('email', )

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Пароли не совпадают.')
        return cd['password2']

