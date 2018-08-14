from django.contrib.auth.models import User
from django import forms
from .models import Customer
from django.contrib.auth.forms import UserCreationForm


class SignUpForm(UserCreationForm):
    username = forms.CharField(
        max_length=30, required=False,
        help_text='Optional.',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Enter User Name',
                'type': 'text'
            }))
    first_name = forms.CharField(label='First Name',
                                 max_length=30, required=False,
                                 help_text='Optional.',
                                 widget=forms.TextInput(
                                     attrs={
                                         'class': 'form-control',
                                         'placeholder': 'Enter First Name',
                                         'type': 'text'
                                     }))
    last_name = forms.CharField(label='Last Name',
                                max_length=30, required=False,
                                help_text='Optional.',
                                widget=forms.TextInput(
                                    attrs={
                                        'class': 'form-control',
                                        'placeholder': 'Enter First Name',
                                        'type': 'text'
                                    }))
    email = forms.EmailField(max_length=254,
                             help_text='Required. Inform a valid email address.',
                             widget=forms.EmailInput(
                                 attrs={
                                     'class': 'form-control',
                                     'placeholder': 'Enter Email Address',
                                     'type': 'email'
                                 }))
    password1 = forms.CharField(label='Password', widget=
    forms.TextInput(attrs=
    {
        'class': 'form-control',
        'placeholder': 'Enter Password',
        'type': 'password'
    }
    )
                                )
    password2 = forms.CharField(label='Confirm Password', widget=
    forms.TextInput(attrs=
    {
        'class': 'form-control',
        'placeholder': 'Enter Confirm Password',
        'type': 'password'
    }
    )
                                )

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2',)


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer

        fields = (
             'phone', 'address', 'gender'
        )
