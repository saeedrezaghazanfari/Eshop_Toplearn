from django import forms
from django.core import validators
from django.contrib.auth.models import User

class EditForm(forms.Form):
    firstName = forms.CharField(
        label='نام',
        widget=forms.TextInput(attrs={'placeholder':'نام خود را وارد کنید','autofocus':'autofocus'})
    )
    lastName = forms.CharField(
        label='فامیل',
        widget=forms.TextInput(attrs={'placeholder':'فامیل خود را وارد کنید','autofocus':'autofocus'})
    )
    password = forms.CharField(
        label='رمز عبور',
        widget=forms.PasswordInput(attrs={'placeholder':'رمز عبور خود را وارد کنید'})
    )

class loginForm(forms.Form):
    user_name = forms.CharField(
        label='نام کاربری',
        widget=forms.TextInput(attrs={'placeholder':'نام کاربری خودرا وارد کنید','autofocus':'autofocus'})
    )
    password = forms.CharField(
        label='رمز عبور',
        widget=forms.PasswordInput(attrs={'placeholder':'رمز عبور خود را وارد کنید'})
    )

    # def clean_user_name(self):
    #     user_name = self.cleaned_data.get('user_name')
    #     is_exist_user = User.objects.filter(username=user_name).exists()
    #     if not is_exist_user:
    #         raise forms.ValidationError('کاربری با این نام وجود ندارد')
    #     return user_name


class registerForm(forms.Form):

    user_name = forms.CharField(
        label='نام کاربری',
        widget=forms.TextInput(attrs={'placeholder': 'نام کاربری خودرا وارد کنید' , 'autofocus':'autofocus'}),
        validators=[
            validators.MaxLengthValidator(limit_value=15, message='نام کاربری نباید بیش از 15 کاراکتر باشد'),
            validators.MinLengthValidator(limit_value=4, message='نام کاربری نباید کمتر از 4 کاراکتر باشد'),
        ]
    )
    email = forms.CharField(
        label='ایمیل',
        widget=forms.TextInput(attrs={'placeholder':'ایمیل خودرا وارد کنید'})
    )
    password = forms.CharField(
        label='رمز عبور',
        widget=forms.PasswordInput(attrs={'placeholder':'رمز عبور خودرا وارد کنید'}),
        validators=[
            validators.MinLengthValidator(limit_value=5, message='رمز عبور بلندتری وارد کنید'),
            validators.MaxLengthValidator(limit_value=20, message='رمز عبور نهایت میتواند 20 کاراکتر باشد')
        ]
    )
    repassword = forms.CharField(
        label='تکرار رمز عبور',
        widget=forms.PasswordInput(attrs={'placeholder':'رمز عبور خودرا دوباره وارد کنید'})
    )
    def clean_user_name(self):
        user_name = self.cleaned_data.get('user_name')
        is_exists = User.objects.filter(username=user_name).exists()
        if is_exists:
            raise forms.ValidationError('نام کاربری دیگری وارد کنید')
        return user_name

    def clean_email(self):
        email = self.cleaned_data.get('email')
        is_exist = User.objects.filter(email=email).exists()
        if is_exist:
            raise forms.ValidationError('ایمیل دیگری وارد کنید')
        return email

    def clean_repassword(self):
        password = self.cleaned_data.get('password')
        repassword = self.cleaned_data.get('repassword')
        if not password == repassword:
            raise forms.ValidationError('باید دو رمز عبور یکی باشند')
        return password