# -*- coding: utf-8 -*-
from django import forms

# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
class RegistrationForm(forms.Form):
        name=forms.CharField(label="Имя",max_length=25)
        lastname=forms.CharField(label="Фамилия",max_length=25)
        phonenumber=forms.CharField(label="Телефон",min_length=13,max_length=13,widget=forms.TextInput(
            attrs={
                'type':'text',
                'placeholder':'** *** ********',

            }
        ))
        email=forms.EmailField()
        password = forms.CharField(label="Пароль", widget=forms.PasswordInput(),max_length=15,min_length=6)
        passwordreapit = forms.CharField(label="Пароль повторно", widget=forms.PasswordInput(),max_length=15,min_length=6)






        def clead_phonenumber(self):
            date=self.changed_data['phonenumber']
            if int(date):
                raise  forms.ValidationError("Только числа")
            return date

        def clean(self):
            cleaned_date=super(RegistrationForm,self).clean()
            password=cleaned_date.get('password')
            passwordreapit=cleaned_date.get('passwordreapit')

            if password!=passwordreapit:
                self.add_error("password","Пароли не совпадают")


class LoginForm(forms.Form):
    email=forms.EmailField()
    password=forms.CharField(label="Пароль", widget=forms.PasswordInput(),max_length=15, min_length=6)
