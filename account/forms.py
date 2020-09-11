from django import forms
from django.contrib.auth.models import User
from .models import Profile
from core_logic.models import Wallet

class RegForm(forms.ModelForm):
    """This form is for registration we use 2 passwords
    and then check if it's equal to each other via 
    clean_password2() function"""
    password = forms.CharField(label='Password',
                               widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat password',
                                widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'email')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']


class SetUserForm(forms.ModelForm):
    """This is the form for editing profile,
    specially User model"""
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name')


class SetProfileForm(forms.ModelForm):
    """This is the form for editing profile,
    specially Profile model"""
    class Meta:
        model = Profile
        fields = ('photo',)


class SetWalletForm(forms.ModelForm):
    class Meta:
        model = Wallet
        fields = ('courency',)
