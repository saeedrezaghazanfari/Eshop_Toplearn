
from django import forms
from django.core import validators

class contactUs_form(forms.Form):

    username = forms.CharField(
        label='نام کاربری',
        widget=forms.TextInput(attrs={'placeholder':'نام', 'class':'form-control'}),
        validators=[validators.MaxLengthValidator(120,'نام نباید از 120 کاراکتر بیشتر باشد.')]
    )

    email = forms.CharField(
        label='ایمیل',
        widget=forms.EmailInput(attrs={'placeholder':'ایمیل', 'class':'form-control'}),
        validators=[validators.MaxLengthValidator(120, 'ایمیل نباید از 120 کاراکتر بیشتر باشد.')]
    )

    subject = forms.CharField(
        label='عنوان',
        widget=forms.TextInput(attrs={'placeholder':'عنوان', 'class':'form-control'})
    )

    msg = forms.CharField(
        label='متن پیام',
        widget=forms.Textarea(attrs={'placeholder':'متن پیام', 'class':'form-control', 'cols': 5, 'rows':10})
    )
