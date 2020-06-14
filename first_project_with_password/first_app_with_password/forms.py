from django import forms
from django.core import validators
from django.contrib.auth.models import User
from first_app_with_password.models import UserProfileInfoModel

class UserForm(forms.ModelForm):
    botcatcher = forms.CharField(required=False, widget=forms.HiddenInput, validators=[validators.MaxLengthValidator(0)])
    username = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput())
    confirm_password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password']

    def clean(self):
        clean_all = super().clean()
        password = clean_all['password']
        confirm_password = clean_all['confirm_password']
        if password != confirm_password:
            raise forms.ValidationError('Password mismatch!')

class UserProfileInfoForm(forms.ModelForm):
    portfolio_site = forms.URLField(required=False, widget=forms.TextInput)
    class Meta():
        model = UserProfileInfoModel
        fields = ['portfolio_site', 'profile_pic']

    def clean_portfolio_site(self):
        clean_all = super().clean()
        portfolio_site = clean_all['portfolio_site']
        if '://' not in portfolio_site and portfolio_site != '':
            portfolio_site = 'http://'+portfolio_site
        return portfolio_site
