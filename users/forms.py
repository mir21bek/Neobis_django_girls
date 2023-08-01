from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from django import forms
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

User = get_user_model()


class CreateUserForm(UserCreationForm):
    email = forms.EmailField(
        label=_('email'),
        max_length=255,
        widget=forms.EmailInput(attrs={'autocomplete': 'email'})
    )

    class Meta:
        model = User
        fields = ('username', 'email')

    def clean_email(self):
        email = self.cleaned_data.get('email')
        username = self.cleaned_data.get('username')
        if email and User.objects.filter(email=email).exclude(username=username).exists():
            raise forms.ValidationError('Такой email уже используется в системе')
        return email

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields['username'].widget.attrs.update({'placeholder': 'придумайте свой ник'})
            self.fields['email'].widget.attrs.update({'placeholder': 'напишите свой почтовый адрес'})
            self.fields['password1'].widget.attrs.update({'placeholder': 'придумайте свой пароль'})
            self.fields['password2'].widget.attrs.update({'placeholder': 'повторите пароль'})
            self.fields[field].widget.attrs.update({'class': 'form-control', 'autocomplete': 'off'})


class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields['username'].widget.attrs['placeholder'] = 'Логин пользователя'
            self.fields['password'].widget.attrs['placeholder'] = 'пароль пользователя'
            self.fields['username'].label = 'Логин пользователя'
            self.fields[field].widget.attrs.update({'class': 'form-control', 'autocomplete': 'off'})