from django import forms

from ecommarce.models import Order


class OrderForm(forms.ModelForm):
    name = forms.CharField(label='Full Name',
                           max_length=30, required=True,
                           help_text='Optional.',
                           widget=forms.TextInput(
                               attrs={
                                   'class': 'form-control',
                                   'placeholder': 'Enter Your FullName',
                                   'type': 'text'
                               }))
    phone = forms.CharField(label='Phone number',
                            max_length=15, required=True,
                            help_text='Optional.',
                            widget=forms.TextInput(
                                attrs={
                                    'class': 'form-control',
                                    'placeholder': 'Enter Your Phone Number',
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
    address = forms.CharField(label='Address', max_length=254, required=True,
                              help_text='Required. Inform a valid address.',
                              widget=forms.Textarea(
                                  attrs={
                                      'class': 'form-control',
                                      'placeholder': 'Enter Your House and Road number',
                                      'type': 'text'
                                  }))
    area = forms.CharField(label='Area',max_length=100,required=True,
                           help_text='Required. Inform a valid Area Name.',
                           widget=forms.TextInput(
                               attrs={
                                   'class': 'form-control',
                                   'placeholder': 'Enter Your Area Address',
                                   'type': 'text'
                               }))

    class Meta:
        model = Order
        fields = ('name', 'phone',  'email','address', 'area', 'quantity', 'delivery_Method')
